from flask import Flask
from flask_frozen import Freezer
from ctflorals.blueprints import ctflorals



app = Flask(__name__)
app.register_blueprint(ctflorals)
app.config['FREEZER_DESTINATION'] = "../build"
freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
