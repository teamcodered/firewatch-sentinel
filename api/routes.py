from flask import current_app as app
from .models import db, DroneDevice, SensorDevice, Observation, SensorObservation, DroneImageObservation, Case

from flask_potion import ModelResource

class ObservationResource(ModelResource):
    class Meta:
        model = Observation

class SensorObservationResource(ModelResource):
    class Meta:
        model = SensorObservation

class DroneImageObservationResource(ModelResource):
    class Meta:
        model = DroneImageObservation

class SensorDeviceResource(ModelResource):
    class Meta:
        model = SensorDevice

class DroneDeviceResource(ModelResource):
    class Meta:
        model = DroneDevice

class CaseResource(ModelResource):
    class Meta:
        model = Case
