import sqlite3
from flask import Flask, render_template, redirect

app = Flask(__name__)

TEMPLATES_AUTO_RELOAD = True

connection = sqlite3.connect('hw8.db')


def get_db_connection():
    db = sqlite3.connect('hw8.db')
    db.row_factory = sqlite3.Row
    return db


@app.route("/")
def index():
    return redirect("/unique_name")


@app.route("/unique_name")
def get_unique_name():
    db = get_db_connection()

    rows = db.execute("SELECT FirstName FROM customers GROUP BY FirstName")     # DISTINCT is also an option

    return render_template('unique_name.html', rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
