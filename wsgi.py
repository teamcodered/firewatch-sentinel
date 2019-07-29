import os
from api import create_app
from analytics import make_celery
from analytics.tasks import setup_tasks
from analytics.routes import setup_routes

app = create_app()
celery = make_celery(app)
setup_tasks(celery)
setup_routes(app, celery)

port = os.getenv('PORT', 5000)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = port)