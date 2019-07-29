from flask import current_app as app
from .models import db, DroneDevice, SensorDevice, Observation, SensorObservation, DroneImageObservation, Case, NationalWeatherServiceFeed, FIRMSDataEntry

from flask_potion import ModelResource

class ObservationResource(ModelResource):
    class Meta:
        model = Observation
        name = 'observation'

class SensorObservationResource(ModelResource):
    class Meta:
        model = SensorObservation
        name = 'sensor-observation'

class DroneImageObservationResource(ModelResource):
    class Meta:
        model = DroneImageObservation
        name = 'drone-observation'

class SensorDeviceResource(ModelResource):
    class Meta:
        model = SensorDevice
        name = 'sensor'

class DroneDeviceResource(ModelResource):
    class Meta:
        model = DroneDevice
        name = 'drone'

class CaseResource(ModelResource):
    class Meta:
        model = Case
        name = 'case'


class NWSFeedResource(ModelResource):
    class Meta:
        model = NationalWeatherServiceFeed
        name = 'nws-feed'

class FIRMSFeedResource(ModelResource):
    class Meta:
        model = FIRMSDataEntry
        name = 'nasa-firms-feed'
