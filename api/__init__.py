from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    api = Api(app)    

    with app.app_context():
        from . import routes
        from . import models
        db.create_all()

        # Add admin models
        admin = Admin(app, name = 'firewatch sentinel', template_mode = 'bootstrap3')
        admin.add_view(ModelView(models.SensorDevice, db.session))
        admin.add_view(ModelView(models.DroneDevice, db.session))
        admin.add_view(ModelView(models.NationalWeatherServiceFeed, db.session))
        admin.add_view(ModelView(models.Observation, db.session))
        admin.add_view(ModelView(models.SensorObservation, db.session))
        admin.add_view(ModelView(models.DroneImageObservation, db.session))
        admin.add_view(ModelView(models.Case, db.session))

        api.add_resource(routes.DroneDeviceResource)
        api.add_resource(routes.SensorDeviceResource)
        api.add_resource(routes.ObservationResource)
        api.add_resource(routes.DroneImageObservationResource)
        api.add_resource(routes.SensorObservationResource)
        api.add_resource(routes.CaseResource)

        api.add_resource(routes.NWSFeedResource)
                
        return app