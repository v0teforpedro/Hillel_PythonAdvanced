from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return '<h3>INDEX</h3>'


@app.route("/avr_data")
def get_avr_data():
    with open('hw.csv', 'r') as reader:

        next(reader)
        people = 0
        height = 0
        weight = 0

        for line in reader:
            try:
                field1, field2, field3 = line.split(',')
                people += 1
                height += float(field2)
                weight += float(field3)
            except ValueError:
                continue

        # convert pounds and inches into kgs and cm's
        avg_height = format((height / people) * 2.54, '.2f')
        avg_weight = format((weight / people) * 0.4536, '.2f')

    return render_template('avr_data.html', height=avg_height, weight=avg_weight, people=people)


@app.route("/requirements")
def get_requirements():
    with open('requirements.txt', 'r') as reader:
        content = reader.read()

    return render_template('requirements.html', text=content)


app.run(debug=True)
