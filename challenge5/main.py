from flask import Flask, render_template
from datetime import datetime

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
    return render_template("kanye.html")


if __name__ == '__main__':
    app.run(debug=True, port=1234)
