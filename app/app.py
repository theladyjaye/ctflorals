from flask import Flask
from ctflorals.blueprints import ctflorals

app = Flask(__name__)
app.register_blueprint(ctflorals)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
