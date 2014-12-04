from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fb_id = db.Column(db.Integer)
    username = db.Column(db.String(80), unique=True)
    rapGodPoints = db.Column(db.Integer, default=0)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)


class Rap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Rap %r>' % (self.title)


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    line1 = db.Column(db.String(1000))
    line2 = db.Column(db.String(1000))
    isPending = db.Column(db.Boolean, default=True)

    rapID = db.Column(db.Integer)
    lineIndex = db.Column(db.Integer)

    userID = db.Column(db.Integer)
    owner = db.Column(db.String(80))

    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def __init__(self, line1, line2, lineIndex, rapID, userID, owner):
        self.line1 = line1
        self.line2 = line2
        self.lineIndex = lineIndex
        self.rapID = rapID
        self.userID = userID
        self.owner = owner

    def __repr__(self):
        return '<Lines %r\n\t%r>' % (self.line1, self.line2)


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
