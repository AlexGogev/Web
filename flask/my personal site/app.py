from flask import Flask, render_template

app = Flask(__name__)

#shift + refresh in chrome is fresh reset without cache
#https://html5up.net/ free templates
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/card")
def card():
    return render_template("card/index.html")
if __name__ == "__main__":
    app.run(debug=True)