from flask import Blueprint, request

from app.libs.libs import do_response
from app.controllers.wallet_controller import create_wallet, get_wallet, get_wallets


wallet_route = Blueprint('wallet', __name__)


@wallet_route.route('/create', methods=['POST'])
async def create_wallet_route():
    """ Create a wallet. """
    try:
        data = request.json
        user_id = data.get('user_id')
        wallet_type = data.get('type')

        wallet, message = await create_wallet(user_id, wallet_type)
        if not wallet:
            return do_response(400, message)
        return do_response(201, message, wallet.serialize())
    except Exception as e:
        return do_response(500, str(e))
    
@wallet_route.route('/get/<user_id>/<wallet_type>', methods=['GET'])
async def get_wallet_route(user_id: int, wallet_type: str):
    """ Get a wallet. """
    try:
       
        wallet, message = await get_wallet(user_id, wallet_type)
        if not wallet:
            return do_response(404, message)
        return do_response(200, message, wallet.serialize())
    except Exception as e:
        return do_response(500, str(e))
    
@wallet_route.route('/get/<user_id>', methods=['GET'])
async def get_wallets_route_user(user_id: int):
    """ Get all wallets for a user. """
    try:
        wallets, message = await get_wallets(user_id)
        if not wallets:
            return do_response(404, message)
        return do_response(200, message, wallets)
    except Exception as e:
        return do_response(500, str(e))

@wallet_route.route('/get_all_wallet', methods=['GET'])
async def get_wallets_route():
    """ Get all wallets. """
    try:
        wallets, message = await get_wallets()
        if not wallets:
            return do_response(404, message)
        return do_response(200, message, wallets)
    except Exception as e:
        return do_response(500, str(e))
