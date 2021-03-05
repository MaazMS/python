1. What is the default host port and port of Flask?  
Flask default host is a localhost (127.0.0.1), and the default port is 5000.   
       
1. How to change default host and port in Flask?  
```  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```          
 
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
1. How to use a HTTP methods in Flask?     
HTTP is the hypertext transfer protocol which is considered as the foundation of the data transfer in the world wide web.  
flask need to provide several HTTP methods for data communication such as GET,POST,PUT,DELETE,     
  
method | description 
|---|---|
GET | Used to fetch the specified resource
POST | Used to create new data at the specified resource
PUT |Used to create new data or replace existing data at the specified resource
DELETE |Used to delete existing data at the specified resource     
```   
Example  @app.route('/',methods = ['POST', 'GET']) 
def function_name(): 
    return "hello"   
```  
   