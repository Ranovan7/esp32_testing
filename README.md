# Flask Project Template (python 3.5 and above)

### Misc.
make sure 'libpq-dev gcc build-essential libssl-dev python3-dev libffi-dev' installed in server (assuming linux)

### Basics

1. Fork/Clone
2. Activate a virtualenv
3. Install the requirements

### Set Environment Variables

Create .env file using the format from .env-template

Generate Secret Key using below command:

```sh
$ python -c 'import secrets; print(secrets.token_urlsafe())'
```

### Create DB

Create the databases and user in `psql`, then grant privileges on db to user:

```sh
$ psql
# create database <database_name>;
# create user <username> with encrypted password '<password>';
# grant all privileges on database <database_name> to <username>;
# \q
```

Create the tables and run the migrations:

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
```

Upgrade DB (when changes occur to 'project/models.py')

```sh
$ python manage.py db migrate
$ python manage.py db upgrade
```

### Run the Application

```sh
$ python manage.py runserver
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)
