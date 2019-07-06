from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest, HTTPException

from src.flask_app.exceptions import CustomAppException


class AppFactory(object):
    def create(self):
        app = Flask(__name__)

        @app.errorhandler(HTTPException)
        def handle_generic_http_exceptions(e):
            return jsonify({
                "error": str(e)
            }), e.code

        @app.errorhandler(CustomAppException)
        def unhandled_meteor_errors(e):
            raise BadRequest(str(e))

        @app.route("/")
        def raise_error_endpoint():
            msg = 'some bad msg'
            raise CustomAppException(msg)

        return app
