### file
Files are where we organize or store our data.  
We use the open method which will return a File object
 f= open("file name", "mode", "buffer") 

 buffer = 4096 or 8092 

this buffer is a is  integer value that we pass in which is internally used to do buffering when we are reading and writing   
to a file.If you don't pass in any number by default 4096 or 8092 will be used by the Python virtual machine.     
#### w
If you use `w` for the right mode which is to write to a file then if the file has some contents already all those contents   
will be deleted and our contents whatever we are writing now will be written right from the beginning of the file.   

#### r
Read mode is to read the file right from the beginning of the file all the way to the end.    

#### a
use append more the current contents of the file will not be deleted and you can add new content to the file at the end   
of the current contents.    

#### w+ 
is for right and read you can do right and read if you open it up.  

### R+ 
is ofr read and you can do read write and append.  

### A+ 
is for appending and reading and there is also exclusive mode to.  

####  exclusive creation mode
1) Once you open a file in this mode a new file will be created for you exclusively.   
2) if a file already exists with the same exact name then an error will be thrown.  

**Note**  If you are dealing with binary files then you just have to append B at the end of each of these modes.  

#### multiple strings
``` 
# you can give any condtion we use `#`.
# open the file for writing
f = open("multiple_strings.txt", "w")
print("Enter the thext (if type # on prompt the it is stop. )")
txt = ''
while(txt !='#'):
    txt = input()
    f.write(txt+"\n")
f.close()
``` 

#### OS module
python give uses a library called OS module which has a sub module called path and that path has a method called is file   
that we can use to check if a file exists. This is file Method returns a boolean true and false.     
we can use the sys module to exit out of our program.  

### pickle 
pickle module serialize an object into a file using dump(object_name,file_name)  
pickle module deserialized an object using load(file_name)  


 
 
