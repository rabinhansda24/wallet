from app.db import db
from app.models.user_model import UserModel


async def create_user(phone_number: str):
    """ Create a new user. """

    if not phone_number:
        return None, "Phone number is required."
    
    user = UserModel(phone_number=phone_number)
    db.session.add(user)
    db.session.commit()

    return user.serialize(), "User created successfully."