from  flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/sucess/<name>')
def user_name(name):
    return 'Welcome %s ' %name

@app.route('/user_name',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return  redirect(url_for('user_name',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('user_name', name=user))
if __name__ == '__main__':
    app.run(debug = True)