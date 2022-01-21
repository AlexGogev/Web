"""
C:\path\to\app>set FLASK_APP=hello.py   -tells flask the name of the file that contain the server
python -m flask run or just: flask run
 python3 -m venv venv  :   py -3 -m venv venv
 venv\Scripts\activate

export day 35
https://pythontutor.com/live.html#mode=edit live debug
decorators day 54 449,450
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route("/<string:name>/<int:age>")
def greet(name, age):
    return f"hello {name} you are {age}"



if __name__ == "__main__":  #instead of terminal -flask run
    app.run(debug=True) #activates live server refresher