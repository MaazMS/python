"""
For run the program in the browser http://127.0.0.1:5050/Accept_dynamic_variable/Maaz
This program is show how to run variable at runtime.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/Accept_dynamic_variable/<name1><name2>')
def hello_world(name1,name2):
    return 'two name %s%S'% name1 %name2


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
