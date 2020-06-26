from flask import Flask, render_template, request, redirect, url_for ,abort

# initialize the flask appliction
app = Flask('__name__')


@app.route('/')
def index():
   return render_template('form.html')


@app.route('/login',methods=['POST','GET'])
def login_flask():
    if request.method == 'POST' and request.form['nm'] == 'Maaz':
        return redirect(url_for("success"))
    else:
        abort(401)

# redirect (url_for(success)) . success have the function name if function name is different it give error
# success1 is the url. if you try to access directly the function success use http://127.0.0.1:5000/success1
@app.route('/success1')
def success():
   return "User name is Maaz"

if __name__ == '__main__':
   app.run(debug = True)