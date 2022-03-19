
# Challenge 5 == return a random kanye west quote from http://localhost:1234/kanye
# decided to use https://api.kanye.rest/

from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)


@app.route('/')
def index():
    print('index_should_be_here')
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', date_time=date_time)


@app.route('/kanye')
def home():
    print("Hi, it's Kanye again")
    quote = requests.get('https://api.kanye.rest/')
    return render_template("kanye.html", quote=quote.json())


if __name__ == '__main__':
    app.run(debug=True, port=1234, host='0.0.0.0')
