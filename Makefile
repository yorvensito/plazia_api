# Makefile para Plazia API

run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

test:
	python manage.py test

lint:
	ruff . --fix

start:
	gunicorn plazia_api.wsgi:application --bind 0.0.0.0:8000

collectstatic:
	python manage.py collectstatic --noinput

docs:
	open http://localhost:8000/api/docs/

build-docker:
	docker build -t plazia-api .

run-docker:
	docker run -p 8000:8000 plazia-api
