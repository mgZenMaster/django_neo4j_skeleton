# Skeleton for Django with mySQL on Docker

You can use this to quickly get started with developing for Django with neo4j on Docker. The
purpose of this skeleton is, to make this as hassle-free as possible, avoiding race-conditions
etc. so you can concentrate on development and not container orchestration.

The docker-compose.yml will set everything up for you, so you are running with two containers,
one having Django and the other running mySQL. There is an entrypoint script, that makes sure
to wait until the database really is there before starting Django.

So just run `docker-compose up`, wait some time, and then you can connect to Django via
`http://localhost:8000`, neo4j web is mapped to `localhost:7474` and Bolt protocol to `localhost:7687`
(standard ports for neo4j)

The root directory of this project will be mapped into the Django container, so every code change
you make will be immediately active in the container.

To use this for your own projects you will probably want to rename "myapp" and "django_neo4j_skeleton"
in all the important places and also the directories. Just do a full text search for both strings, you'll
find everything that needs to be changed.

Renaming will also change the name of the containers, databases, the volume and the network, so there
will be no conflicts between parallel projects. You only have to change the port mapping manually in
`docker-compose.yml`, if you want to run stuff in parallel.

## Admin

You will find some example models in `myapp/models.py`, those models are also imported into the Django
admin (see `myapp/admin.py`). That way you can put some data in the database. Unfortunately it is not
possible to set relationships in the Django admin AFAIK, so you have to set that up yourself with custom
views.

Go to `http://localhost:8000/admin/` and log in with username `admin` and password `pass`.

## License

This code is provided under GNU General Public License v3.0
