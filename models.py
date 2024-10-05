# models.py will contain all the database models ( how we interact with the database )
# we use Flask-SQLAlchemy to create a python class which represents some kind of entry/row for the database/some kind of a table and we define the different columns and data that the class/objects will be 

from config import db

# this class represents the "heroes" table in the database
class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nulable=False)
    super_name = db.Column(db.String(80), nullable=False)

    # linking each hero to their power by establishing a relationship with the HeroPower model
    # backref allows accessibility to the hero object from the HeroPower table using 'hero' attribute
    # the 'cascade' option ensures that deleting a hero will also delete their power
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    
# define a function that can take all the
# attributes in the object above and convert
# it into a python dictionary which we can
# then convert into json, something that we
# can pass from our API

# the way we communicate in API is using
# something known as json which looks like
# a python dictionary. We will be passing
# json back and forth so that API will
# return json and we will send json to the
# API for creating our different objects

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }
    

# this class represents the "powers" table in the database
class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(80), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "hero": self.hero.to_dict(), # returns the related hero's details as a dictionary
            "power": self.power.to_dict(), # returns the related power's details as a dictionary
        }
