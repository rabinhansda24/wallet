from app.db import db
from app.models.wallet_model import WalletModel


async def create_wallet(user_id: int, wallet_type: str) -> WalletModel:
    """ Create a wallet for a user. """

    if WalletModel.query.filter_by(user=user_id, type=wallet_type).first():
        return None, "User already has a wallet of this type" # Wallet already exists

    wallet = WalletModel(user=user_id, type=wallet_type)
    try:
        db.session.add(wallet)
        db.session.commit()
        return wallet, "Wallet created successfully"
    except Exception as e:
        return None, str(e)
    

async def get_wallet(user_id: int, wallet_type: str = None) -> WalletModel:
    """ Get a wallet for a user. """

    wallet = WalletModel.query.filter_by(user=user_id, type=wallet_type).first()
    if not wallet:
        return None, "Wallet not found"
    return wallet, "Wallet found"


async def get_wallets(user_id: int = None) -> list:
    """ Get all wallets for a user. """

    if user_id is None:
        wallets = WalletModel.query.all()
        if not wallets:
            return None, "No wallets found"
        return [wallet.serialize() for wallet in wallets], "Wallets found"

    wallets = WalletModel.query.filter_by(user=user_id).all()
    if not wallets:
        return None, "No wallets found"
    return [wallet.serialize() for wallet in wallets], "Wallets found"