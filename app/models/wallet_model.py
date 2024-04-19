from app.db import db


class WalletModel(db.Model):
    """ Wallet model. """

    __tablename__ = 'wallets'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)

    transactions = db.relationship('TransactionModel', backref='wallets', lazy=True)

    __table_args__ = (db.UniqueConstraint('user', 'type', name='unique_wallet'),)


    def __repr__(self):
        return f'<Wallet {self.id}>'
    

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user,
            'type': self.type,
            'balance': self.balance
        }