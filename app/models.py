from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    trait = db.Column(db.String(120))
    cost = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Character {}>'.format(self.name) 