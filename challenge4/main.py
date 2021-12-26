from flask import Flask, render_template

app = Flask(__name__)

# make a server that serves an index.html file from http://localhost:1234/count


@app.route('/forwardslash')
def forwardslash():
    return 'we are hot'


@app.route('/count')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=1234)
