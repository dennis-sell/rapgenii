from application import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    owner = db.Column(db.String(80))
    answer = db.Column(db.String(1000), nullable=True)
    responder = db.Column(db.String(80), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, question, owner):
        self.question = question
        self.owner = owner

    def __repr__(self):
        return '<Question %r>' % self.question

    def addAnswer(self, answer, responder):
        self.answer = answer
        self.responder = responder
        self.completed = True

##
# Create your own models here and they will be imported automaticaly. or
# use a model per blueprint.

##
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(80), unique=True)
#     password = db.Column(db.String(80))

#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def __repr__(self):
#         return '<User %r>' % (self.username)

##
# class Log(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime)
#     hostname = db.Column(db.String(20))
#     flagger = db.Column(db.Boolean)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     user = db.relationship('User', backref='log', lazy='dynamic')

#     def __init__(self, time, uptime, hostname, flagger, user_id):
#         self.returns = 0
#         self.errors = 0
#         self.time = time
#         self.hostname = hostname
#         self.flagger = flagger
#         self.user_id = user_id

#     def __repr__(self):
#         return '<Log %r>' % (self.hostname)
