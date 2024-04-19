from datetime import datetime
import os
from app.db import db
from app.models.wallet_model import WalletModel
from app.models.transaction_model import TransactionModel
from app.libs.queue.task_processor import add_transaction_to_queue

MINIMUM_BALANCE = os.getenv('MINIMUM_BALANCE', 0.0)

def create_transaction(user_id: int, wallet_id: int, amount: float, is_credit: bool):
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
    
def process_transaction(user_id: int, wallet_id: int, amount: float, is_credit: bool):
    add_transaction_to_queue(create_transaction, user_id, wallet_id, amount, is_credit)
    return True, "Your transaction is being processed. Please check back later for the status."
    

async def get_transactions(user_id: int, wallet_id: int) -> list:
    """ Get all transactions for a wallet. """

    transactions = TransactionModel.query.filter_by(user=user_id, wallet=wallet_id).all()
    return [transaction.serialize() for transaction in transactions], "Transactions found"


async def get_transaction_total_in_period(user_id: int, wallet_id: int, start_date: datetime, end_date: datetime) -> dict:
    """ Get the total amount of transactions in a period. """
    try:
        transaction_info = TransactionModel.transaction_total_in_period(user_id, wallet_id, start_date, end_date)

        if not transaction_info:
            return None, "No transactions found"
        
        return transaction_info, "Transactions found"
    except Exception as e:
        return None, str(e)