from flask import (Flask, render_template)

app = Flask(__name__)



@app.route('/')
def hello():
    return f"<h1>What's good friends?</h1>"


@app.route('/hello/<name>')
def greeting(name):
    return f"<h1>How's it going {name}???</h1>"


@app.route('/sup')
@app.route('/yo_dude')
def sup_dude():
    return render_template('index.html')

