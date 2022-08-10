
# Challenge 5 == return a random kanye west quote from http://localhost:1234/kanye
# decided to use https://api.kanye.rest/

from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

visit_count = 0
POST_count = 0


@app.route('/')
def index():
    global visit_count
    print('index_should_be_here')
    visit_count += 1
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', date_time=date_time)


@app.route('/kanye')
def home():
    print("Hi, it's Kanye again")
    quote = requests.get('https://api.kanye.rest/')
    return render_template("kanye.html", quote=quote.json())


@app.route('/visits')
def visits():
    print("Wow, your popular this session.")
    awyeah = visit_count
    return render_template("visits.html", visit_count=visit_count)


@app.route('/count', methods=['GET'])
def count_GET():
    print("Check out this POSTage!")
    mooo = POST_count
    return render_template("count.html", POST_count=POST_count)


@app.route('/count', methods=['POST'])
def count_POST():
    global POST_count
    POST_count += 1
    print("Something was POSTed!")
    return render_template("count.html", POST_count=POST_count)


'''
@app.route('/count', methods=['GET'])
def count():
    global POST_count
    print("Check out this POSTage!")
    mooo = POST_count
    return render_template("count.html", POST_count=POST_count)

'''

'''
@app.route('/count', methods=['GET', 'POST'])
def count():
    global POST_count
    if flask.request.method == 'POST':
        POST_count += 1
    else:
        print("Check out this POSTage!")
        moo = POST_count
    return render_template("count.html", POST_count=POST_count)
'''

if __name__ == '__main__':
    app.run(debug=True, port=1234, host='0.0.0.0')
