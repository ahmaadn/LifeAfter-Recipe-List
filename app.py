import csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/api/data')
def data():
    # kamu bisa mendapatkan file csv di
    # https://docs.google.com/spreadsheets/d/19Y1tZdekS7OOAr6Bii3K_E8wskNudagu1H3wmQ_CzjI/edit#gid=828755875

    with open('static/data/data.csv') as csv_file:
        df = csv.DictReader(csv_file, delimiter=',')
        data = []
        for row in df:
            row.pop("S.No.")
            data.append(row)

        return {"data": data}



# if __name__ == '__main__':
#     app.run(debug=True)
