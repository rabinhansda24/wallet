from flask import Blueprint, request

from app.libs.libs import do_response
from app.controllers.transaction_controller import create_transaction, get_transactions


transaction_route = Blueprint('transaction', __name__)


@transaction_route.route('/create', methods=['POST'])
async def create_transaction_route():
    """ Create a transaction. """
    try:
        data = request.json
        user_id = data.get('user_id')
        wallet_id = data.get('wallet_id')
        amount = data.get('amount')
        is_credit = data.get('is_credit')

        transaction, message = await create_transaction(user_id, wallet_id, amount, is_credit)
        print(transaction)
        if transaction is None:
            return do_response(400, message)
        return do_response(201, message, transaction.serialize())
    except Exception as e:
        return do_response(500, str(e))
    

@transaction_route.route('/get/<user_id>/<wallet_id>', methods=['GET'])
async def get_transactions_route(user_id: int, wallet_id: int):
    """ Get all transactions for a wallet. """
    try:
        transactions, message = await get_transactions(user_id, wallet_id)
        return do_response(200, message, transactions)
    except Exception as e:
        return do_response(500, str(e))