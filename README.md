# HealthRecords application 



## Setup

The first thing to do is to clone the repository:

```sh
$ git remote add origin git@github.com:WeronikaJodkowska/todo_tms.git
$ cd todo_tms
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```

