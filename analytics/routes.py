from flask import make_response

def setup_routes(app, celery):
    print('setting up app routes ..')

    @app.route('/start-download/<string:region>')
    def download_and_save(region):
        print('downloading from url: {}'.format(region))
        return make_response('Downloading data for region: ' + region, 200)  

    print('app routes setup complete ..')   

    