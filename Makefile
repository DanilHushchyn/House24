MANAGE = python manage.py

run:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

worker:
	celery -A House24 worker -l info

dumpdata:
	$(MANAGE) dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > db.json

startapp:
	$(MANAGE) flush --no-input
	$(MANAGE) migrate --no-input
	$(MANAGE) loaddata data_init.json
	gunicorn House24.wsgi:application --bind 0.0.0.0:8000