from datetime import datetime
from sqlalchemy import func, case
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
    
    @classmethod
    def transaction_total_in_period(cls, user_id: int, wallet_id: int, start_date: datetime, end_date: datetime):
        """ Get the total amount of transactions in a period. """
        
        # Query to sum amounts conditionally based on credit or debit and count transactions
        result = db.session.query(
            func.sum(case((cls.is_credit == True, cls.amount), else_=0)).label('credit_total'),
            func.sum(case((cls.is_credit == False, cls.amount), else_=0)).label('debit_total'),
            func.count(case((cls.is_credit == True, cls.amount), else_=0)).label('credit_count'),
            func.count(case((cls.is_credit == False, cls.amount), else_=0)).label('debit_count')
        ).filter(
            cls.user == user_id,
            cls.wallet == wallet_id,
            cls.created_at >= start_date,
            cls.created_at <= end_date
        ).one()

        if not result:
            return None
        
        return {
            'credit_total': result.credit_total,
            'debit_total': result.debit_total,
            'credit_count': result.credit_count,
            'debit_count': result.debit_count
        }

    
    def serialize(self):
        return {
            'id': self.id,
            'user': self.user,
            'wallet': self.wallet,
            'amount': self.amount,
            'is_credit': self.is_credit,
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S')
        }
