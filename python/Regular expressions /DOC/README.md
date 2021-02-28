#### Regular expressions  
Regular expressions also known as` REGX `are a bunch of characters or a pattern that will create to search for a string   
within a given string or to validate the given string For example we can use a regular expression to validate the email  
that is entered by the user a password that the user enters etc.    
   
#### Sequence Characters  
1. The regular expression syntax define some special characters called sequence characters that we can use to match a single   
character in a given string.  
2. All these sequence characters start with a backwards slash.   
3.`\d` This stands for ANY digit 0 to 9.   
4. `\D` that does the opposite any non-digit character   
5. `\s` Which stands for white space it matches white space in the given string   
6. `\S` opposite of non white space   
7. `\W` for any alpha numeric value it could be any digit or character A to Z \W   
8. `\W` non alpha numeric characters   
9.`\b` is a space around words   
10. `\A` matches only at the start of the string it will do a search right at the beginning of the string   
11.`\Z` matches only at the end of the string.    

#### search

The search method takes a regular expression and it searches for that format in the given string and it returns the very   
first sub-string within the given string that matches that pattern once the result is returned back.  
```eg 
import re

str = "Take up one idea, One idea at a time"
result1 = re.search(r'o\w\w', str)
result2 = re.search(r'i\w', str)
print(result1.group())
one
id
```
#### group 
Group is a method on the result that comes back which will give us the exact string that matches the given pattern.   
The result will be none on that NONE. You cannot invoke with the group Method only when it is not none.    

#### findall()  
findall() it searches the given string for that pattern right from the beginning all the way to the end.And it will return   
all the sub-strings that match the given expression as a list so the list will contain every substring in the given string   
that matches the given regular expression. And if none of the substrings in the given string matches the regular expression    
it will return a empty.     
``` 
Example 

import re
str = "Take up one idea, one idea at a time"
result = re.findall(r'o\w\w', str)
result1 = re.findall(r'i\w', str)
print(result)
print(result1)
['one', 'one']
['id', 'id', 'im']
```
#### match() 
match() method, takes the regular expression and it searches for that pattern in the given string right at the beginning   
of the string. That's it right at the beginning if it matches it will return that substring. If not it will return None.   
``` 
Example 
import re
str = "Take up one idea, one idea at a Time"
result = re.match(r'o\w\w', str)
result1 = re.match(r'T\w', str)
print(result)
print(result1.group())
None
Ta
``` 

#### split
The split Method split the given string into a list of strings using the regular expression that we pass in as the limiter   
plus one or more digits.  
``` 
import re
str = "Take up 123 idea, one idea at 132 time"
result = re.split(r'\d+', str)
print(result) 
['Take up ', ' idea, one idea at ', ' time']
```
#### sub 
The submitter does a replace all that is it will substitute the given string with a new string. The second parameter here   
is whatever we want to replace with the first parameter.first parameter is sub-string.  

#### quantifiers  
1. So far you have done single character matching using the sequence characters we can use quantifiers to match multiple characters.   
2. `+` plus to specify one or more repetitions of the preceding regular expression. for example \d+ means one or more digits.   
3. `*`if you use star quantifier it means zero or more repetitions of the preceding regular expression
4. `?` question marks means zero or one repetition of the preceding regular expression within flower brackets.
5. If you use m this means exactly the `{m}` occurrences of the preceding regular expression 
6. {m,n} m is the minimum number of occurrences, n is the maximum number of occurrences by default `m` will be zero and   
`n` will beat infinity if you don't specify anything.     

####  Special Character   

1. `\` Starting with backward slash which is a escape character if you want to use a backwards slash or any other special   
characters or within the regular expression then you have to escape it using the backward slash.  
2. `.`   dot operator which matches any character except a new line. 
3. `^`  used to match a given regular expression at the beginning of a string.
4. `$` regular expression match  at the end of the string.  
5. `[...]` For example if you give A to B  
6. `[^...] it matches every characters except the ones in square brackets so here we can specify a range.  
7. `(...)` 
8. `(R|S)` 

 