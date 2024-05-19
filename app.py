from flask import Flask
from flask import request



app = Flask(__name__)

"""
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return 'Hello, POST!'
    return 'Hello, GET!'
"""

# alternatively:
@app.get('/')
def hello_get():
    return 'Hello, GET!'

@app.post('/')
def hello_post():
   return 'Hello, POST!'