from app import db
from datetime import datetime

# PRODUCTION COMPANY TABLE
class Production(db.Model):
    __tablename__ = 'production'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'The Production company is {}'.format(self.name)


# MOVIES TABLE
class Movie(db.Model):
    __tablename__ = 'movie'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False, index=True)
    directors = db.Column(db.String(600))
    cast = db.Column(db.String(600))
    avg_rating = db.Column(db.Float)
    image = db.Column(db.String(100), unique=True)

    # ESTABLISH RELATIONSHIP
    prod_id = db.Column(db.Integer, db.ForeignKey('production.id'))

    def __init__(self, name, directors, cast, avg_rating, image, prod_id):

        self.name = name
        self.directors = directors
        self.cast = cast
        self.avg_rating = avg_rating
        self.image = image
        self.prod_id = prod_id

    def __repr__(self):
        return '{} by {}'.format(self.name, self.directors)

