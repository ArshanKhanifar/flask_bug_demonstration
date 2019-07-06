from src.flask_app.app_factory import AppFactory


if __name__ == '__main__':
    app = AppFactory().create().run()
