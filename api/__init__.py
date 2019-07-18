from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    api = Api(app)    

    with app.app_context():
        from . import routes
        db.create_all()
        api.add_resource(routes.DroneDeviceResource)
        api.add_resource(routes.SensorDeviceResource)
        api.add_resource(routes.ObservationResource)
        api.add_resource(routes.DroneImageObservationResource)
        api.add_resource(routes.SensorObservationResource)
        api.add_resource(routes.CaseResource)
        return app