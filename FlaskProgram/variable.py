"""
For run the program in the browser http://127.0.0.1:5050/Accept_dynamic_variable/Maaz
This program is show how to run variable at runtime.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/Accept_dynamic_variable/<name>')
def hello_world(name):
    return 'Hello %s !' % name


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
