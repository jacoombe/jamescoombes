
#app/__init__.py
from flask import Flask
from backend import simple_page
app = Flask(__name__)
from app import views
app.config.from_object('app.configuration.DevConfig')
app.register_blueprint(simple_page)

# Now we can access the configuration variables via app.config["VAR_NAME"].
