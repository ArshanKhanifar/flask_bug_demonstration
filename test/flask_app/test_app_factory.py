from werkzeug.exceptions import BadRequest
from src.flask_app.app_factory import AppFactory


class TestApp(object):

    def test_error_endpoint(self):
        # given
        app = AppFactory().create()
        client = app.test_client()

        # when
        rv = client.get('/')

        # then
        assert "some bad msg" in rv.get_json()["error"]
        assert rv.status_code == BadRequest.code
