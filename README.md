# autobets
Django/Nuxt reference application


Getting started
---------------

This setup requires Docker.

```
docker-compose up -d
docker-compose exec django bash
./autobets/manage.py migrate
./autobets/manage.py createsuperuser

```

Once everything is up and running open http://localhost:8000 in your browser for backend.
Once everything is up and running open http://localhost:3000 in your browser for frontend.


polling tasks are not setup to run when app is up using docker.
to run polling tasks set in django settings.py
```
make cmd_django
cd autobets
celery -A autobets worker -l info
```
```
in another shell 
make cmd_django
cd autobets
celery -A autobets beat -l info
```






