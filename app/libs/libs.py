from flask import make_response, jsonify

def do_response(status_code: int, message: str = None, data: any = None):
    """ Return a response. """
    return make_response(jsonify({"message": message, "data": data}), status_code)