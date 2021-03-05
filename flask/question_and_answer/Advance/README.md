

1. What do you mean by template engines in the Flask framework?  
A template is a file that contains two types of data, i.e., static and dynamic. Dynamic data in a template is populated  
during run time.  
  



  

1. How to serve static files in Flask?   
Dynamic web applications also need static files.That’s usually where the CSS and JavaScript files are coming from.  
`url_for('static', filename='style.css')`  
The file has to be stored on the filesystem as static/style.css.   

1. What is Routing and how to use?  
Routing is the process of selecting a path for traffic in a network or between or across multiple networks.  
```   
from flask import Flask
# The decorator is telling our @app that whenever a user visits our app domain (myapp.com) at the given
# route(), execute the hello_world() function.
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'  
# Flask application is started by cal1ing run() function 
```  
 
1. What is redirect and how to use?  
Returns a response object that redirects the client to the target location.  
```  
@app.route('/user_name',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return  redirect(url_for('user_name',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('user_name', name=user))
```
1. What is template and how to use?  
Flask provides us the render_template() function which can be used to render the external HTML file to be returned as    
the response from the view function.  
```  
@app.route('/hello/<user>')
def user_name(user):
    return render_template('hello.html', name=user)
```

1. what is abort and how to use?
abort function raises HTTP error, it will have the same behavior.    
```  
@app.route('/login',methods=['POST','GET'])
def login_flask():
    if request.method == 'POST' :
        return redirect("http://www.example.com")
    else:
        abort(401)
```
