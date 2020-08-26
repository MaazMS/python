from flask import Flask

app = Flask(__name__)


# The decorator is telling our @app that whenever a user visits our app domain (myapp.com) at the given
# route(), execute the hello_world() function.
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
# Flask application is started by claaing run() function
