from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    salt = db.Column(db.String(250), nullable=False)
    rank = db.Column(db.SmallInteger, default=0)
    points = db.Column(db.Integer, default=0)
    description = db.Column(db.String(250))

class League(db.Model):
    __tablename__ = 'league'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    principle = db.Column(db.Float, nullable=False)
    goal = db.Column(db.Float)
    term_start = db.Column(db.DateTime, nullable=False)
    term_end = db.Column(db.DateTime, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=True)
    min_users = db.Column(db.SmallInteger)
    max_users = db.Column(db.SmallInteger)
    min_stocks = db.Column(db.SmallInteger)
    max_stocks = db.Column(db.SmallInteger)

class Placement(db.Model):
    __tablename__ = 'placement'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    league = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    rank = db.Column(db.SmallInteger, default = 0)
    value = db.Column(db.Float, nullable=False)

class Investment(db.Model):
    __tablename__ = 'investment'
    id = db.Column(db.Integer, primary_key=True)
    placement = db.Column(db.Integer, db.ForeignKey('placement.id'), nullable=False)
    symbol = db.Column(db.String(250), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    term_start = db.Column(db.DateTime, nullable=False)
    term_end = db.Column(db.DateTime, nullable=False)
    start_price = db.Column(db.Float, nullable=False)
    last_price = db.Column(db.Float, nullable=False)
    last_price_time = db.Column(db.DateTime, nullable=False)