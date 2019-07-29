import os
import urllib
import datetime

def setup_tasks(celery):

    @celery.task()
    def download_firms_data(url):
        if not os.path.isdir('./tmp'):
            os.mkdir('./tmp')
        # opener = urllib.request.build_opener()
        filename = datetime.datetime.now();
        print('downloading FIRMS data: {}' % (filename))
        urllib.request.urlretrieve(url, 'firms_' + filename + '.csv')
        print('downloaded FIRMS data.')    

    @celery.task()
    def save_to_object_store():
        pass

    @celery.task()
    def read_to_db():
        pass