from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('index_should_be_here')
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    return 'the temperature is hot'

if __name__ == '__main__':
    app.run(debug=True, host="192.168.1.43")

