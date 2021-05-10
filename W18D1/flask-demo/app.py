from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return f"<h1>What's good friends?</h1>"


@app.route('/sup')
def sup_dude():
    return render_template('index.html')