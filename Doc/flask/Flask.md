1) what is flask.     
Flask is a lightweight WSGI (Web Server Gateway Interface) web application framework.A Web-Application Framework or Web Framework is the collection of modules and libraries that helps the developer to write applications without writing the low-level codes such as protocols, thread management, etc.     

2) what is  Web Server Gateway Interface.   
 It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request. WSGI is a Python standard described in detail in PEP 3333.    

3) Who use flask.   
799 companies reportedly use Flask in their tech stacks, including Netflix, reddit, and Lyft.      


4) what did that code do?.   
 1. First we imported the Flask class. An instance of this class will be our WSGI application.
 2. we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single   
  module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name  
  will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, 
  and so on.    
 3. We then use the route() decorator to tell Flask what URL should trigger our function.     
 4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser. 

5) how to run flask   
Just save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.   
To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable: 

6) Externally Visible Server.  
server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.   

arbitrary : andom choice .example"a country under arbitrary government"   


If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:    


7 )What to do if the Server does not Start   
 1. Old Version of Flask  
      upgrade to newer Flask versions   
 2. Invalid Import Name    
    The FLASK_APP environment variable is the name of the module to import at flask run. In case that module is incorrectly named you will get an import error.  
 3. The most common reason is a typo or because you did not actually create an app object. 

8) why Debug Mode (helpful debugger if things go wrong.)    
The flask script is nice to start a local development server, but you would have to restart it manually after each change to your code. That is not very nice and Flask can do better.    

* This does the following things:   

 a. it activates the debugger   

 b. it activates the automatic reloader    

 c. it enables the debug mode on the Flask application.   
 
##### Attention
interactive debugger does not work in forking environments (which makes it nearly impossible to use on production servers), it still allows the execution of arbitrary code. This makes it a major security risk and therefore it must never be used on production machines.    




###### Routing 
uses a meaningful URL they can remember and use to directly visit a page.     
You can make parts of the URL dynamic and attach multiple rules to a function.  

###### Variable Rules  
add variable sections to a URL by marking sections with <variable_name>.   
Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.     
Converter types:   
string : (default) accepts any text without a slash  
int : accepts positive integers   
float : accepts positive floating point values   
path : like string but also accepts slashes   
uuid : accepts UUID strings   







###### Unique URLs / Redirection Behavior 
This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.  
 * `canonical URL` projects endpoint has a trailing slash. It’s similar to a folder in a file system.eg./projects/    



###### URL Building 
It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.This can do using url_for() function.   



###### HTTP Methods    
You should familiarize yourself with the HTTP methods as you work with Flask. By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.

###### Static Files    
Dynamic web applications also need static files.i.e CSS and JavaScript files.save this file on static folder.   
Just create a folder called static in your package or next to your module and it will be available at /static on the application.   
To generate URLs for static files, use the special 'static' endpoint name:   
url_for('static', filename='style.css')   
The file has to be stored on the filesystem as static/style.css.   

#### Accessing Request Data

* Context Locals :    
 Imagine the context being the handling thread. A request comes in and the web server decides to spawn a new thread (or something else, the underlying object is capable of dealing with concurrency systems other than threads). When Flask starts its internal request handling it figures out that the current thread is the active context and binds the current application and the WSGI environments to that context (thread). It does that in an intelligent way so that one application can invoke another application without breaking.    

 The solution is creating a request object yourself and binding it to the context. The easiest solution for unit testing is to use the test_request_context() context manager. In combination with the with statement it will bind a test request so that you can interact with it.  


###### The Request Object¶ 

What happens if the key does not exist in the form attribute? In that case a special KeyError is raised. You can catch it like a standard KeyError but if you don’t do that, a HTTP 400 Bad Request error page is shown instead. So for many situations you don’t have to deal with that problem.   

To access parameters submitted in the URL (?key=value) you can use the args attribute:   

searchword = request.args.get('key', '')   
We recommend accessing URL parameters with get or by catching the KeyError because users might change the URL and presenting them a 400 bad request page in that case is not user friendly.   

###### File Uploads
enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.

Uploaded files are stored in memory or at a temporary location on the filesystem. You can access those files by looking at the files attribute on the request object. Each uploaded file is stored in that dictionary. It behaves just like a standard Python file object, but it also has a save() method that allows you to store that file on the filesystem of the server.    

If you want to know how the file was named on the client before it was uploaded to your application, you can access the filename attribute.   
If you want to use the filename of the client to store the file on the server, pass it through the secure_filename() function that Werkzeug provides for you:   

##### Cookies   


The cookies attribute of request objects is a dictionary with all the cookies the client transmits. If you want to use sessions, do not use the cookies directly but instead use the Sessions in Flask that add some security on top of cookies for you.   
Note that cookies are set on response objects. Since you normally just return strings from the view functions Flask will convert them into response objects for you. If you explicitly want to do that you can use the make_response() function and then modify it.     
 set a cookie at a point where the response object does not exist yet. 
use [Deferred Request Callbacks](https://flask.palletsprojects.com/en/1.1.x/patterns/deferredcallbacks/#deferred-callbacks)   
 



######  Redirects and Errors  
To redirect a user to another endpoint, use the redirect() function.    
to abort/terminate a request early with an error code, use the abort() function.   
By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator.   
Note the 404 after the render_template() call. This tells Flask that the status code of that page should be 404 which means not found.   

##### About Responses

If you want to get hold of the resulting response object inside the view you can use the make_response() function.   
if the return value is a dict, jsonify() is called to produce a response. The logic that Flask applies to converting return values into response objects is as follows:   
 1. If a response object of the correct type is returned it’s directly returned from the view.    
 2. If it’s a string, a response object is created with that data and the default parameters.   
 3. If it’s a dict, a response object is created using jsonify.
 4. If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form (response, status), (response, headers), or (response, status, headers). The status value will override the status code and headers can be a list or dictionary of additional header values.   

If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a response object.   


##### APIs with JSON

If you return a dict from a view, it will be converted to a JSON response.    


##### Sessions  

in addition to the request object there is also a second object called session which allows you to store information specific to a user from one request to the next.    
What this means is that the user could look at the contents of your cookie but not modify it, unless they know the secret key used for signing.
 Flask will take the values you put into the session object and serialize them into a cookie.     

* How to generate good secret keys

A secret key should be as random as possible. Your operating system has ways to generate pretty random data based on a cryptographic random generator. Use the following command to quickly generate a value for Flask.secret_key (or SECRET_KEY):   
$ python -c 'import os; print(os.urandom(16))'   
b'_5#y2L"F4Q8z\n\xec]/'    



##### Message Flashing 
Flask provides a really simple way to give feedback to a user with the flashing system.
The flashing system basically makes it possible to record a message at the end of a request and access it on the next (and only the next) request. This is usually combined with a layout template to expose the message.    
To flash a message use the flash() method, to get hold of the messages you can use get_flashed_messages()    

##### Hooking in WSGI Middleware  

1. what WSGI middleware.  
A WSGI middleware component is a Python callable that is itself a WSGI application, but may handle requests by delegating to other WSGI applications.    
To add WSGI middleware to your Flask application, wrap the application’s wsgi_app attribute. For example, to apply Werkzeug’s ProxyFix middleware for running behind Nginx.    

##### Using Flask Extensions   
Extensions are packages that help you accomplish/fulfil common tasks.. For example, Flask-SQLAlchemy provides SQLAlchemy support that makes it simple and easy to use with Flask.    





