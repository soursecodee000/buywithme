release: python manage.py runserver
web: gunicorn storefront.wsgi
worker: celery -A storefront worker