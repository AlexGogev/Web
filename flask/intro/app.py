from flask import Flask, render_template
from datetime import datetime
import requests
import json

app = Flask(__name__)

#shift + refresh in chrome is fresh reset without cache
#https://html5up.net/ free templates


@app.route("/")
def index():
    time = datetime.now().strftime("%H:%M:%S")
    return render_template("index/index.html", time=time)


@app.route("/card")
def card():
    return render_template("card/index.html")


@app.route('/jinja')
def jinja():
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    year = datetime.now().strftime("%Y")
    return render_template("jinja/jinja.html", now_time=now, cur_year=year)

@app.route('/guess/<name_guess>')
def name(name_guess):
    response = requests.get(url=f"https://api.genderize.io?name={name_guess}").json()
    name = response["name"].title()
    gender = response["gender"]
    return render_template("jinja/genderize.html", name=name, gender=gender)


@app.route("/blog")
def blog():
    response = requests.get(url="https://api.npoint.io/157c873b7ecc4fea48d2").json()
    return render_template("jinja/blog.html", response=response)


"""
@app.route("/<string:name>/<int:age>")
def greet(name, age):
    return f"hello {name} you are {age}"
"""

if __name__ == "__main__":  #instead of terminal -flask run
    app.run(debug=True) #activates live server refresher