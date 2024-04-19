from flask import Blueprint, request
from datetime import datetime

from app.libs.libs import do_response
from app.controllers.transaction_controller import create_transaction, get_transactions, get_transaction_total_in_period


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
    
@transaction_route.route('/get/total_in_period', methods=['POST'])
async def get_transaction_total_in_period_route():
    """ Get the total amount of transactions in a period. """
    try:
        data = request.json
        user_id = data.get('user_id')
        wallet_id = data.get('wallet_id')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

        transaction_info, message = await get_transaction_total_in_period(user_id, wallet_id, start_date, end_date)
        if transaction_info is None:
            return do_response(400, message)
        return do_response(200, message, transaction_info)
    except Exception as e:
        return do_response(500, str(e))