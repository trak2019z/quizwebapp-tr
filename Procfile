release: python manage.py migrate
web: daphne mysite.asgi:application --port $port --bind 0.0.0.0
worker: python manage.py runworker channels -v2