from flask import Flask

from app.db import db
from app.routes.hello_route import hello_route
from app.routes.user_route import user_route
from app.routes.wallet_route import wallet_route
from app.routes.transaction_route import transaction_route



def initialize_routes(app: Flask):
    """ Initialize routes. """

    app.register_blueprint(hello_route)
    app.register_blueprint(user_route, url_prefix='/api/v1/users')
    app.register_blueprint(wallet_route, url_prefix='/api/v1/wallet')
    app.register_blueprint(transaction_route, url_prefix='/api/v1/transactions')


def initialize_database(app: Flask):
    """ Initialize database. """

    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()


def initialize_cors(app: Flask):
    """ Initialize CORS. """

    pass