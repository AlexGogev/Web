from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!'


#C:\path\to\app>set FLASK_APP=hello.py   -tells flask the name of the file that contain the server
#python -m flask run or just: flask run
# python3 -m venv venv  :   py -3 -m venv venv
# venv\Scripts\activate
#export day 35

if __name__ == "name":
    app.run()