import os
from app.db import db
from app.models.wallet_model import WalletModel
from app.models.transaction_model import TransactionModel

MINIMUM_BALANCE = os.getenv('MINIMUM_BALANCE', 0.0)

async def create_transaction(user_id: int, wallet_id: int, amount: float, is_credit: bool) -> TransactionModel:
    """ Create a transaction for a wallet. """

    try:
        wallet = WalletModel.query.get(wallet_id)
        if not wallet:
            return None, "Wallet not found"

        if is_credit:
            wallet.balance += amount
        else:
            print(f"MINIMUM_BALANCE: {MINIMUM_BALANCE}")
            if (wallet.balance - amount < int(MINIMUM_BALANCE)):
                return None, "Insufficient balance"
            wallet.balance -= amount

        transaction = TransactionModel(user=user_id, wallet=wallet_id, amount=amount, is_credit=is_credit)
    
        db.session.add(transaction)
        db.session.commit()
        return transaction, "Transaction created successfully"
    except Exception as e:
        return None, str(e)
    

async def get_transactions(user_id: int, wallet_id: int) -> list:
    """ Get all transactions for a wallet. """

    transactions = TransactionModel.query.filter_by(user=user_id, wallet=wallet_id).all()
    return [transaction.serialize() for transaction in transactions], "Transactions found"