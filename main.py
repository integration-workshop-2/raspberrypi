from flask import Flask
from flask_cors import CORS

from server.routes.vital_signs_sensors import vital_signs_sensors_bp


app = Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(blueprint=vital_signs_sensors_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="10.42.0.3", port=6000)
