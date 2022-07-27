from flask import Flask, render_template

app = Flask(__name__)

with open('home.html', "r+") as file:
    r = file.read()


@app.route('/')
def index():
    return f"{r}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8181)
