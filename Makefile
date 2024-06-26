run_async:
	ASGI=true \
	python manage.py runserver

run:
	ASGI=false \
	python manage.py runserver