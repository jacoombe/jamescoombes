
#app/__init__.py
from flask import Flask

app = Flask(__name__)
from app import views
app.config.from_object('app.configuration.DevConfig')

# Now we can access the configuration variables via app.config["VAR_NAME"].
