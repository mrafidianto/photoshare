# Makefile

init:
	pdm install

# Initialize the Django app
dev:
	pdm run src/manage.py runserver

collectstatic:
	pdm run src/manage.py collectstatic

# Initialize user admin
createadmin:
	pdm run src/photoshare/manage.py createsuperuser

tailwind-watch:
	bunx tailwindcss -i ./src/a_core/static/css/tailwind.css -o ./src/a_core/static/css/style.css --watch

tailwind-minify:
	bunx tailwindcss -i ./src/a_core/static/css/tailwind.css -o ./src/a_core/static/css/style.css --minify