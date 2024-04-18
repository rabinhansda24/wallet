from flask import Flask

from app.routes.hello_route import hello_route



def initialize_routes(app: Flask):
    """ Initialize routes. """

    app.register_blueprint(hello_route)


def initialize_database(app: Flask):
    """ Initialize database. """

    pass


def initialize_cors(app: Flask):
    """ Initialize CORS. """

    pass