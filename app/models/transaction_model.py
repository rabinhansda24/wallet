from datetime import datetime

from sqlalchemy import func
from app.db import db


class TransactionModel(db.Model):
    """ Transaction model. """

    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    wallet = db.Column(db.Integer, db.ForeignKey('wallets.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    is_credit = db.Column(db.Boolean, nullable=False) # True if credit, False if debit
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f'<Transaction {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'user': self.user,
            'wallet': self.wallet,
            'amount': self.amount,
            'is_credit': self.is_credit,
            'created_at': self.created_at
        }
