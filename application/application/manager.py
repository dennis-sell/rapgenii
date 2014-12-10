from application import app
from flask import render_template, jsonify
from application.models import *
from flask import Flask, session, redirect, url_for, escape, request
from flask_oauthlib.client import OAuth, OAuthException
import random
from __init__ import facebook

@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        return render_template('info/hello.html', username=escape(session['username']))
    return render_template('info/index.html', title='Stress Reliever')


@app.route('/home/')
def home():
    return render_template("info/home.html", title="Home")

@app.route('/raps/<int:rapID>')
def show_rap(rapID):
    rap = Rap.query.filter(Rap.id == rapID)
    lines = Line.query.filter(Line.rapID == rapID)
    return render_template("info/rap.html", rap=rap, lines=lines)

@app.route('/add_rap', methods=['POST'])
def add_rap():
    print 'hello'
    print request.form['rap']
    print db
    try:
        r = Rap(request.form['rap'], False)
        db.session.add(r)
        db.session.commit()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/add_line', methods=['POST'])
def add_line():
    try:
        l = Line(request.form['line'], escape(session['username']))
        db.session.add(l)
        db.session.commit()
        return jsonify(success=True)
    except:
        return jsonify(success=False)


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
    print me.data
    if not User.query.filter_by(fb_id=me.data['id']):
        email = me.data['email'].split("@")[0]
        u = User(me.data['id'], email, 0)
        db.session.add(u)
        db.session.commit()
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

# @app.route('/add_post', methods=['POST'])
# def add_question():
#     try:
#         q = Question(request.form['question'], escape(session['username']))
#         db.session.add(q)
#         db.session.commit()
#         return jsonify(success=True)
#     except:
#         return jsonify(success=False)

# @app.route('/get_stress')
# def get_stresses():
#     weights = Question.query.filter(Question.completed==False). \
#                              filter(Question.owner!=escape(session['username'])).all()
#     if weights:
#         final_stress = random.choice(weights)
#         return jsonify({'question':final_stress.question, 'id' : final_stress.id})
#     return jsonify({})

# @app.route('/add_response', methods=['POST'])
# def add_response():
#     pk = request.form['id']
#     response = request.form['response']
#     email_responder = escape(session['username'])
#     try:
#         q = Question.query.filter_by(id=pk).first()
#         q.addAnswer(response, email_responder)
#         db.session.commit()
#         return jsonify(success=True)
#     except:
#         return jsonify(sucess=False)
