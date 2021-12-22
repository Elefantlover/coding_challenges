from flask import Flask, render_template

app = flask(__name__)

# make a server that serves an index.html file from http://localhost:1234/count


@app.route('/count')
def index():


if __name__ == '__main__':
    app.run(debug=True, port=1234)
