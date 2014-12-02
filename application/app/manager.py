from application import app
from flask import render_template, jsonify
from application.models import *
from flask import Flask, session, redirect, url_for, escape, request
import random

@app.route('/')
@app.route('/index/')
def index():
    if 'username' in session:
        return render_template('info/hello.html', username=escape(session['username']))
    return render_template('info/index.html', title='Stress Reliever')

@app.route('/signin', methods=['POST'])
def signin():
    session['username'] = request.form['email']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/add_post', methods=['POST'])
def add_question():
    try:
        q = Question(request.form['question'], escape(session['username']))
        db.session.add(q)
        db.session.commit()
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/get_stress')
def get_stresses():
    weights = Question.query.filter(Question.completed==False). \
                             filter(Question.owner!=escape(session['username'])).all()
    if weights:
        final_stress = random.choice(weights)
        return jsonify({'question':final_stress.question, 'id' : final_stress.id})
    return jsonify({})

@app.route('/add_response', methods=['POST'])
def add_response():
    pk = request.form['id']
    response = request.form['response']
    email_responder = escape(session['username'])
    try:
        q = Question.query.filter_by(id=pk).first()
        q.addAnswer(response, email_responder)
        db.session.commit()
        return jsonify(success=True)
    except:
        return jsonify(sucess=False)
