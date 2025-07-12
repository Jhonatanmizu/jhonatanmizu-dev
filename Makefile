tailwind-watch:
	npm run tailwind:watch

django-runserver:
	uv run manage.py runserver

dev:
	make -j 2 tailwind-watch django-runserver
