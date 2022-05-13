.PHONY: runserver


runserver:
	python manage.py runserver


.DEFAULT_GOAL := runserver