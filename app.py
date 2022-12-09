import csv
import requests
from flask import Flask, render_template

app = Flask(__name__)
SHEET_ID = "19Y1tZdekS7OOAr6Bii3K_E8wskNudagu1H3wmQ_CzjI"
SHEET_NAME = "Recipe%20List"

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/api/data')
def data():
    # kamu bisa mendapatkan file csv di
    # https://docs.google.com/spreadsheets/d/19Y1tZdekS7OOAr6Bii3K_E8wskNudagu1H3wmQ_CzjI/edit#gid=828755875    
    URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

    # write
    r = requests.get(URL)
    open('static/data/temp.csv', 'wb').write(r.content)

    # read
    with open('static/data/temp.csv', 'r') as csv_file:
        df = csv.DictReader(csv_file, delimiter=',')
        data = []
        for row in df:
            if row['S.No.']:
                row.pop("S.No.")
                data.append(row)

        csv_file.close()
        return {"data": data}


if __name__ == '__main__':
    app.run()
