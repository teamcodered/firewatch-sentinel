import os
import urllib
import datetime
from flask import make_response
from .core import FIRMSDataProductNames, FIRMS_VIIRS_RegionDataUrl, FIRMS_MODIS_RegionDataUrl

def setup_routes(app, celery, tasks):
    print('setting up app routes ..')

    @app.route('/viirs/<string:region>')
    def download_and_save(region):
        print('downloading from url: {}'.format(region))
        region_data_url = None
        try:
            region_data_url = FIRMS_VIIRS_RegionDataUrl.Regions[region]
        except KeyError:
            return make_response('Region {} not found in database.'.format(region))
        
        dl_firms_data_task = tasks[0]
        result = dl_firms_data_task.delay(region,region_data_url)
        file = result.wait()
        return make_response('Downloaded and imported data for region: {} into {} '.format(region_data_url, file), 200)  

    print('app routes setup complete ..')   

    