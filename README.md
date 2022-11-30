# HealthRecords 

Health Records - convenient access to health data. 
For in the paper version it is sometimes not only inconvenient to store, but unreliable, 
we created an opportunity to save the data of analyzes and examinations.


## Setup

The first thing to do is to clone the repository:

```sh
git clone git@github.com:WeronikaJodkowska/HealthRecords.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
python3 -m venv venv
source venv/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Create database:
```sh
sudo su postgres
psql
# CREATE USER health WITH PASSWORD 'health' CREATEDB;
# CREATE DATABASE health OWNER health;
# GRANT ALL PRIVILEGES ON DATABASE health TO health;
```

Create base tables in the database:
```sh
python3 manage.py migrate
```

Create a system user:
```sh
python3 manage.py createsuperuser
```

To run the app:
```sh
python3 manage.py runserver
```

