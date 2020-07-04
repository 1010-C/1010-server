#1010-Creators Server

## Local Setup

Create a virtual environment for the project

> python3 -m virtualenv env

Activate virtual environment

> source env/bin/activate

Initialise GIT

> git init

Set git remote

> git remote add origin https://github.com/1010-C/1010-server.git

Pull

> git pull origin master

Install dependencies

Ensure you have postgres installed on your machine.
Check out [this!](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04) guide for linux users.

Create a new database.

> pip install -r requirements.txt

Make sure you have this environment variables set
* DB_NAME (The name of the database you created )
* DB_USERNAME (The user that owns the databas you created. High chances thats its your username ;) )
* DB_PASSWORD (Database password. High chances its your password )
* DB_PORT (You may set this to an empty string, Django knows)
* DB_HOST (You may set this to an empty string, Django knows)

Start up the server

> python3 manage.py runserver

### NOTE : Am explicitly using `python3`

### codificación feliz!
