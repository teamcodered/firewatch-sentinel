from . import db

class Device(db.Model): 
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text, nullable = True)

class SensorDevice(Device):
    __tablename__ = 'sensor'

    deviceId = db.Column(db.String(250), primary_key = True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    observations = db.relationship('SensorObservation', backref = 'sensor', lazy = True, uselist = True)

class DroneDevice(Device):
    __tablename__ = 'drone'
    deviceId = db.Column(db.String(250), primary_key = True)

class Observation(db.Model):
    __tablename__ = 'observation'

    id = db.Column(db.Integer, primary_key = True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    notes = db.Column(db.Text, nullable = True)
    observation_time = db.Column(db.DateTime, nullable = False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable = True)


class SensorObservation(db.Model):
    __tablename__ = 'sensor_observation'

    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column(db.Float, nullable = True)
    humidity = db.Column(db.Float, nullable = True)
    co2 = db.Column(db.Float, nullable = True)
    fire_score = db.Column(db.Float, nullable = True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'), nullable = True)
    observation_id = db.Column(db.Integer, db.ForeignKey('observation.id'), nullable = False)
    observation = db.relationship('Observation', backref = 'sensor_observation', lazy = True, uselist = False)

class DroneImageObservation(db.Model):
    __tablename__ = 'drone_observation'

    id = db.Column(db.Integer, primary_key = True)
    image_object_id = db.Column(db.String(250), nullable = True)
    image_object_url = db.Column(db.String(500), nullable = True)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable = True)
    fire_score = db.Column(db.Float, nullable = True)
    observation_id = db.Column(db.Integer, db.ForeignKey('observation.id'), nullable = False)
    observation = db.relationship('Observation', backref = 'drone_observation', lazy = True, uselist = False)

class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(250), unique = True, nullable = True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    location = db.Column(db.Text)
    state = db.Column(db.String(100), nullable = True)
    country = db.Column(db.String(100), nullable = True)
    description = db.Column(db.Text, nullable = True)

    observations = db.relationship('Observation', backref = 'case', lazy = True)