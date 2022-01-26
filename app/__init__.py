from flask import Flask
from app.routes import home, dashboard, api
from app.db import init_db

def create_app(test_config=None):
    # set up app config
    # the app serves any static resources from the root directory and not from
    # default /static directory
    app = Flask(__name__, static_url_path='/')
    # Trailing slashes are optional and '/dashboard/ and /dashboard' load the same route
    app.url_map.strict_slashes = False
    # app uses the key below when creating server-side sessions
    app.config.from_mapping(
        SECRET_KEY='my_dream_dog'
    )
    
    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    
    init_db()
    
    return app