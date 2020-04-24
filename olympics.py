from flask import Flask, render_template

app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')

    my_reader = csv.DictReader(datafile)

    list_of_dicts = list(my_reader)

    datafile.close()

    return list_of_dicts
olympics_list = convert_to_dict("olympics.csv")

pairs_list = []
for o in olympics_list:
    pairs_list.append( (o['number'], o['country']) )



@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, country = {}, the_title="Country Index")



@app.route('/country/<num>')
def detail(num):
    try:
        olympics_dict = olympics_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Country: {num}</h1>"
    return render_template('country.html', country=olympics_dict, the_title=olympics_dict['country'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
