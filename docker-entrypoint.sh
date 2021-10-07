#!/bin/bash

if [[ ! -f /.initdj ]] ;then

    python /app/waitfordb.py || exit 1

    echo "Making migrations"
    python /app/manage.py makemigrations
    echo "Migrating"
    python /app/manage.py migrate

    CU="from django.contrib.auth.models import User;"
    CU="${CU} User.objects.create_superuser('admin', 'admin@example.com', 'pass')"
    CU="${CU} if User.objects.filter(username='admin').count() == 0 else None"
    echo "${CU}" | python manage.py shell

    touch /.initdj
fi

exec "$@"