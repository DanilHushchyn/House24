gunicorn Diploma.wsgi
celery -A Diploma worker -l info

exec "$@"