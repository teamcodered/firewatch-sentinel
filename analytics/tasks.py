import os
import urllib
import datetime

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


    @celery.task()
    def save_to_object_store():
        pass

    @celery.task()
    def read_to_db():
        pass


    return download_firms_data, save_to_object_store, read_to_db