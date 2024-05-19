Python web dev code: Flask

$ curl -sSL https://install.python-poetry.org | python3
$ poetry completions bash >> ~/.bash_completion
$ poetry init
$ python3 -m venv <~/path/to/project/directory>
$ source ./bin/activate
$ sudo apt install gunicorn
$ gunicorn -w 4 example:app

check the given http
to shut down - Ctrl+C
to quit env - deactivate

running wsgiref server (server.py):
$ python3 -m server
(in another CLI window:) $ ss -ltnup 'sport = :8000'


running Flask app (dev server):

$ sudo apt install python3-flask
$ flask run --port 8000

checking for responces in another CLI window:
$ curl -X GET localhost:8000
$ curl -X POST localhost:8000
