import os
import urllib
import datetime
import csv

from api.models import FIRMSDataEntry as FireDataModel
from api import db

def setup_tasks(celery):

    @celery.task()
    def download_firms_data(region, url):
        if not os.path.isdir('./tmp'):
            os.mkdir('./tmp')
        output_dir = './tmp/'        
        dt_fragment = '{0:%Y_%m_%d_%H_%M_%S}'.format(datetime.datetime.now())
        filename = 'viirs-{}-{}.csv'.format(region, dt_fragment)
        output_file_path = output_dir + filename
        print('dumping file: {} to ./tmp'.format(filename))
        urllib.request.urlretrieve(url, output_file_path)

        with open(output_file_path, 'r') as f:
            csv_reader = csv.reader(f, delimiter = ',')
            line_count = 0
            for row in csv_reader:
                line_count += 1
                if line_count == 1:
                    continue
                fire_entry = FireDataModel(latitude = float(row[0]), longitude = float(row[1]), bright_ti4 = float(row[2]), scan = float(row[3]), track = float(row[4]),
                acq_date = datetime.datetime.strptime(row[5], '%Y-%m-%d'), acq_time = int(row[6]), satellite = row[7], confidence = row[8], version = row[9],
                bright_ti5 = float(row[10]), frp = float(row[11]), daynight = row[12]                
                )
                db.session.add(fire_entry)
                
            db.session.commit()

        return filename


    @celery.task()
    def save_to_object_store():
        pass

    @celery.task()
    def read_to_db():
        pass


    return download_firms_data, save_to_object_store, read_to_db