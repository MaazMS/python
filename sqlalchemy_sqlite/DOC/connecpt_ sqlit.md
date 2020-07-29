## Date and Time Types   
SQLite does not have built-in DATE, TIME, or DATETIME types, and `pysqlite` does not provide out of the box functionality   
for translating values between Python datetime objects and a SQLite-supported format. SQLAlchemy’s own DateTime and     
related types provide date formatting and parsing functionality when SQLite is used.        
   
      
#### SQLite Auto Incrementing Behavior   
Background on SQLite’s autoincrement is at:[here](http://sqlite.org/autoinc.html)       

Key concepts:   

* SQLite has an implicit “auto increment” feature that takes place for any non-composite primary-key column that is        
specifically created using “INTEGER PRIMARY KEY” for the type + primary key.   

* SQLite also has an explicit “AUTOINCREMENT” keyword, that is not equivalent to the implicit autoincrement feature; this    
keyword is not recommended for general use. SQLAlchemy does not render this keyword unless a special SQLite-specific    
directive is used (see below). However, it still requires that the column’s type is named “INTEGER”.                  