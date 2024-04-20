import os
from functools import wraps
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, verify_jwt_in_request

from app.extensions.jwt import jwt
from app.models.user_model import UserModel
from app.models.wallet_model import WalletModel
from app.libs.libs import do_response


def create_token(user_id: int):
    """ Create a new JWT token. """
    expiry = timedelta(minutes=os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 15))
    return create_access_token(identity=user_id, expires_delta=expiry)



@jwt.user_identity_loader
def user_identity_lookup(identity):
    return identity