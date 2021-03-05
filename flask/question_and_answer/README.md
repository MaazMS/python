1. What is Flask?  
Flask is a micro web framework written in Python. It is based on Jinja 2 template engine and Werkzeug WSGI web application library.       
  
1. Is the Flask framework open source?  
Yes, the Flask framework is open-source.   
  
1. What is WSGI?  
WSGI stands for the Web Server Gateway Interface. It describes how a web server communicates with a web application.  
  
1. Who created Flask?  
Armin Ronacher created the Flask framework.  
         
1. Why do we use Flask?
Flask is used to create Web applications using Python programming language.   
Flask is a micro framework that is also used for quick prototyping web and networking based applications.     
  
1. What is the default host port and port of Flask?  
Flask default host is a localhost (127.0.0.1), and the default port is 5000.   
       
1. How to change default host and port in Flask?  
```  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```          
 
1. Why is Flask called a Micro framework?    
Flask is called a micro framework because Flask only provides core features such as request, routing, and blueprints.   
   
1. What do you mean by template engines in the Flask framework?  
A template is a file that contains two types of data, i.e., static and dynamic. Dynamic data in a template is populated  
during run time.  
  
1. Describe the features of Forms extension for Flask(Flask-WTF).   
Forms in Flask can be implemented by using an extension called Flask-WTF.  
It supports data validation, internationalization, and CSRF protection.     

1. How to use a session in Flask?  
Whenever we want to save some data between requests, then we make use of session objects in Flask.   
We can set and get data from the session object.  

````   
fromflask import Flask, session
 
app = Flask(__name__)
 
@app.route('/use_session')
def use_session()
        session['Name'] = {'first': 'Maaz', 'last': 'Shaikh'} 
    return session.get('Name')
 
@app.route('/delete_session')
def delete_session()
    session.pop('Name', None)
    return "removed song from session"
```` 
  
1. How to debug a Flask Application?  
Flask comes with a development server, and the development server has a Debug Mode.  
```  
from flask import Flask 
app = Flask(__name__)
app.run(host='127.0.0.1', debug=True)
```    

What type of Applications can we create with Flask?

Answer: With Flask, we can create almost all types of web applications. We can create Single Page Application, RESTful API based Applications, SAS applications, Small to medium size websites, static websites, Microservices, and serverless apps.