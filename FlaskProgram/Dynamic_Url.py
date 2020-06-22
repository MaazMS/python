"""
url_for() function is used for dynamic building a URL for specific function
Example http://127.0.0.1:5000/admin
        http://127.0.0.1:5000/guest/shaikh
"""

from flask import Flask ,redirect , url_for

app =Flask(__name__)

@app.route('/admin')
def administration():
    return 'administration'

@app.route('/guest/<guest_fun>')
def guest_name(guest_fun):
    return 'Guest name is %s ' % guest_fun

# This function use redirect the url.

@app.route('/user/<user_fun>')
def dynamic_url(user_fun):
    if user_fun == 'admin':
        return redirect(url_for('administration'))
    else:
        return  redirect(url_for('guest_name',guest_fun = user_fun))

if __name__ == '__main__':
      app.run(debug = True )