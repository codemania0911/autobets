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
