from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    print('index_should_be_here')
    now = datetime.now()  # current date and time
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('index.html', date_time=date_time)


@app.route('/temperature')
def temperature():
    return 'the temperature is hot'


@app.route('/params')
def params():
    return 'parameters'


@app.route('/time/<minutes>')
def minutes(minutes):
    x = int(minutes)
    # return current time + minutes
    return f'minutes: {x*2} '


@app.route('/time/<hours>/<minutes>')
def hours(minutes, hours):
    m = int(minutes)
    h = int(hours)
    # return current time + hours + minutes
    return f'hours: {hours}, minutes: {minutes} '


# date with + days route
@app.route('/date/<dateday>')
def dateday(dateday):
    d = int(dateday)
    print('workin on date')
    now = datetime.now()  # current date and time
    d = dateday
    date_month = now.strftime("%m")
    date_year = now.strftime("%Y")

    return render_template('dateday.html', dateday=dateday, date_month=date_month, date_year=date_year)


if __name__ == '__main__':
    app.run(debug=True, port=1234)
