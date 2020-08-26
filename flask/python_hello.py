# Flask uses the Jinja template library to render templates.
""""
To run the template program first create templates folder inside templates folder have html file
The python file outside of template folder.
Step 1 : first run the python program
The output is hello Maaz .
The 'hello' is the html content inside of <h1></h1> .
Maaz is the name pass inside of url
eg http://127.0.0.1:5000/hello/maaz
"""

import os

from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def user_name(user):
    return render_template('hello.html', name=user)

if __name__ == "__main__":
    app.run(debug=True)
