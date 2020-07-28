Q1. What is sqlalchemy. ?   
SQLAlchmey is an open source SQL toolkit and ORM for python programming language.   

Q2. What is full form of ORM ?  
ORM is stands for object relational model.   
Q3. What is ORM. ?      
ORM is programming technique for converting data between incompatible type systems in relational databases and          
object-oriented programming languages.      
![](https://miro.medium.com/max/700/1*9TZHTGKjIyUOAvmQkV1RNA.png)    
Q4. Feature of ORM. ?   
a. Offer a uniform object oriented interface for the progarammers.     
b. Make the db backend migration much easier (from mysql to sql server or others)  
c.Improve the robust of the code(using ORM means less code, and less code means less error)   

Q5. Feature of sqlalchemy   
a. sqlalchemy support ORM and Non-ORM.   

Q6 .What is mapping.? 
* A mapping is nothing but conversion of sql object into python.  
* According to sqlalchemy you can define two types. 
a.  Classical mapping    
b. Declarative mapping    

Q7. What is classical mapping   
This is sqlalchemy's original class mapping api, and is still the base mapping system provide bt the ORM.     
In “classical” form, the table metadata is created separately with the Table construct,      
then associated with the User class via the mapper() function:          
[example](https://docs.sqlalchemy.org/en/13/orm/mapping_styles.html)      

Q8. What is Declarative mapping.?     
Declarative system, the components of the user-defined class as well as the Table metadata to which the class is mapped    
are defined at once.    
That means in classical mapping create user table and then create create class of table and then maaper(table_name, class_name)    
but in declarative only need to create table at once.   

Q9. unit of work
All changes in state between objects and their related rows, called a unit of work.   
    

Q10 . what is Pool. ?       
A connection pool is a standard technique used to maintain long running connections in memory for efficient re-use, as    
well as to provide management for the total number of connections an application might use simultaneously.   

Particularly for server-side web applications, a connection pool is the standard way to maintain a “pool” of active database    
connections in memory which are reused across requests.   

In other word pool is use to the connection of database and application.         
![](https://docs.sqlalchemy.org/en/13/_images/sqla_engine_arch.png)     

Q.11 what is create_engine.?      

Q.12 what is declarative base.?   
The declarative base class wraps the mapper and the MetaData.    

Q.13  what is mapper.?   
The mapper maps the subclass to the table.   
 
Q.14 what is MetaData.?   
MetaData holds all the information about the database and the tables it contains.   

Q.15 what is Session.?     
The Session object also wraps the database connection and transaction.    
TO interact with the database using the Session object.   
The transaction implicitly starts as soon as the Session starts communicating with the database and will remain open     
until the Session is committed, rolled back or closed.    
One way to create a Session object is to use the Session class from the sqlalchemy.orm package.   

Q.16 why use sessionmaker.?   
if use `session = Session(bind=engine)` The Session constructor accepts a number of argument to customize its working.   
If we choose to create Session using this method, we would have to call the Session constructor with the same set of    
parameters over and over again throughout the application.     

* To make things easier, SQLAlchemy provides sessionmaker.   
Q17. what is sessionmaker.?  
sessionmaker class which creates Session class with default arguments set for its constructor.   
You should call call sessionmaker once in your application at the global scope.       

