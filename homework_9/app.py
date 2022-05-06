from flask import Flask, render_template
from webargs.flaskparser import use_kwargs
from webargs import fields
from utils import lookup

app = Flask(__name__)

TEMPLATES_AUTO_RELOAD = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/rates")
@use_kwargs(
    {
        'currency': fields.Str(required=True)
    },
    location='query'
)
def rates(currency):
    quote = lookup(currency)
    return render_template('rates.html', quote=quote)


if __name__ == "__main__":
    app.run(debug=True)
