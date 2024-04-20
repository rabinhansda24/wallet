from flask import Flask

from app.config.config import get_config_by_name
from app.initialize_functions import initialize_routes, initialize_database, initialize_cors
from app.libs.queue.task_processor import start_processing
from app.extensions.jwt import initialize_jwt


def create_app(config_name: str):
    """ Create app. """

    app = Flask(__name__)
    app.config.from_object(get_config_by_name(config_name))

    initialize_routes(app)
    initialize_database(app)
    initialize_cors(app)
    start_processing(app)
    initialize_jwt(app)

    return app