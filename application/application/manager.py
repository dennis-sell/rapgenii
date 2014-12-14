from application import app
from flask import render_template, jsonify
from application.models import *
from flask import Flask, session, redirect, url_for, escape, request
from flask_oauthlib.client import OAuth, OAuthException
import random
import quality_control
from __init__ import facebook

@app.route('/')
def home():
    unfinRaps = Rap.query.filter(Rap.completed == False).all()
    finRaps = Rap.query.filter(Rap.completed == True).all()
    user = None
    if 'user_id' in session:
        user = User.query.filter_by(fb_id=session['user_id']).first()
    return render_template("info/home.html", title="Home", user = user, unfinRaps=unfinRaps, finRaps=finRaps)

@app.route('/raps/<int:rapID>')
def show_rap(rapID):
    rap = Rap.query.filter(Rap.id == rapID).first()
    pending_lines = Line.query.filter(Line.rapID == rapID) \
                               .filter(Line.isPending == True).all()
    pending_lines = quality_control.sort_lines_by_wilson_score(pending_lines)

    accepted_lines = Line.query.filter(Line.rapID == rapID) \
                               .filter(Line.isPending == False) \
                               .order_by(Line.lineIndex.asc()).all()
    user = None
    if 'user_id' in session:
        user = User.query.filter_by(fb_id=session['user_id']).first()
    return render_template("info/rap.html", user=user, rap=rap, pending_lines=pending_lines,
                                                     accepted_lines=accepted_lines)

@app.route('/add_rap', methods=['POST'])
def add_rap():
    try:
        if session['user_id']:
            r = Rap(request.form['rap'])
            db.session.add(r)
            db.session.commit()
        return redirect(url_for('home'))
    except:
        return jsonify(success=False)

@app.route('/add_line', methods=['POST'])
def add_line():
    index = 1 + 2*len(Line.query.filter(Line.rapID == request.form['rapID'],
                                        Line.isPending == False).all())
    rapID = request.form['rapID']
    try:
        l = Line(request.form['line1'], request.form['line2'],
            index, request.form['rapID'], escape(session['user_id']))
        db.session.add(l)
        db.session.commit()
        return redirect(url_for('show_rap', rapID = rapID))
    except:
        return jsonify(success=False)

# THIS IS THE ROUTE I AM USING FOR THE UPVOTES

@app.route('/line/_upvote', methods=['POST', 'GET'])
def upvote_ajax():
    if request.method == 'POST':
        lineID = request.form['lineID']
        line = Line.query.get(lineID)
        line.upvotes += 1
        current_user = User.query.filter_by(fb_id=session['user_id']).first()
        if (current_user and line not in current_user.lines):
            current_user.lines.append(line)
            db.session.add(current_user)
            db.session.commit()
            return jsonify(lineID=lineID)
        else:
            return redirect(url_for('home'))


@app.route('/line/_downvote', methods=['POST', 'GET'])
def downvote_ajax():
    if request.method == 'POST':
        lineID = request.form['lineID']
        line = Line.query.get(lineID)
        line.downvotes += 1
        current_user = User.query.filter_by(fb_id=session['user_id']).first()
        if (current_user and line not in current_user.lines):
            current_user.lines.append(line)
            db.session.add(current_user)
            db.session.commit()
            return jsonify(lineID=lineID)
        else:
            return redirect(url_for('home'))


@app.route('/add_line', methods=['POST'])
def select_best_line():
    if request.method == 'POST':
        rapID = request.form['rapID']
        rap = Rap.query.get(rapID)
        pending_lines = pending_lines(rapID)
        best_line, other_lines = quality_control.best_line(pending_lines)
        if best_line:
            best_line.isPending = False
            db.session.remove(other_lines)
            """ Can you remove a list? If not
            for line in other_lines:
                db.session.remove(line)
            """
            db.session.add(best_line)
            # finishes the line if it reaches the max length
            current_length = len(accepted_lines(rapID)) + 2
            #Plus 2, because the lines that we just added haven't been placed in the database
            if current_length >= rap.max_length:
                rap.completed = True
                db.session.add(rap)
            db.session.commit()


def accepted_lines(rapID):
    return Line.query.filter(Line.rapID == rapID) \
                     .filter(Line.isPending == True).all()

def pending_lines(rapID):
    return Line.query.filter(Line.rapID == rapID) \
                     .filter(Line.isPending == True).all()

@app.route('/login')
def login():
    callback = url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True)
    print callback
    return facebook.authorize(callback=callback)

@app.route('/login/authorized')
def facebook_authorized():
    resp = facebook.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    session['user_id'] = me.data["id"]
    if not User.query.filter_by(fb_id=me.data['id']).first():
        email = me.data['email']
        u = User(me.data['name'], me.data['id'], email)
        db.session.add(u)
        db.session.commit()
    return redirect(url_for('home'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route('/logout')
def logout():
    session.pop('oauth_token', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))
