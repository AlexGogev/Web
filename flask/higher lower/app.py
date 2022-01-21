from flask import Flask
import random

guess_number = random.randint(1,9)
app = Flask(__name__)
string = ""
def indexing():
    for i in range(1,11):
        a =  f"<a href='/{i}'> {i}"
        global string
        string += a

indexing()
@app.route('/')
def index():
    return f'<h1> Guess the number </h1> ' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
           f' <br> {string}'




@app.route("/<int:x>")
def guess_me(x):
    if x < guess_number:
        return f"<h1> To small try again <br>{string}  "
    elif x > guess_number:
        return f"<h1>too big <br> {string}"
    else:
        return "<h1>yes"


print(guess_number)
if __name__ == "__main__":
    app.run(debug=True)