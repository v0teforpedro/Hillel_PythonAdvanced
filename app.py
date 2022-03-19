from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h3>This is Homepage</h3><n></n><h3>Proceed further to: /hello/flask</h3>'

@app.route("/hello")
def hello():
    return "<h2>Proceed further to: /hello/flask</h2>"

@app.route("/hello/flask")
def hello_flask():
    return "<h1>Hello from Flask application!</h1>"


app.run(debug=True)


