
from . import db
import enum


class PropertyModel(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(80))
    num_of_bedrooms = db.Column(db.Integer)
    num_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price=db.Column(db.Float)
    property_type= db.Column(db.String(10))
    description=db.Column(db.String(255))
    property_name=db.Column(db.String(255))

    def __init__(self, title, num_of_bedrooms,num_of_bathrooms,location,price,property_type,description,property_name):
        self.title=title
        self.description=description
        self.num_of_bathrooms=num_of_bathrooms
        self.num_of_bedrooms=num_of_bedrooms
        self.location=location
        self.price=price
        self.property_type=property_type
        self.property_name=property_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
