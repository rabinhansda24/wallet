from app.db import db


class UserModel(db.Model):
    """ User model. """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.phone_number}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number
        }