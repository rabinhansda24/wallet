from flask import Blueprint, request

from app.libs.libs import do_response
from app.controllers.user_controller import create_user

user_route = Blueprint("user_route", __name__)


@user_route.route("/", methods=["POST"])
async def createuser():
    """ Create a new user. """
    try:
        phone_number = request.json.get("phone_number")
        user, message = await create_user(phone_number)

        if not user:
            return do_response(400, message)

        return do_response(201, message, user)
    except Exception as e:
        return do_response(500, str(e))