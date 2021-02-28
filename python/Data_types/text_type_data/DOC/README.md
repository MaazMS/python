 
#### create string using 
1. single quote.  
2. double quote.  
3. triple quotes.   

#### Example of create string   
1. first_name = 'Maaz'   
2. last_name = "shaikh"  
3. full_name = """ My name is 
Maaz Shaikh
"""

#### string operation  
1. `+` operator : It is use to join two string.  
2. `*` operator : It is use to multiple the string.  
3. check value present in string or not. return true or false.  
4. slice string means access string value by index.(index start from zero)   
5. slice string means access string value by index range.  

#### example of operation  
1. `str1 = "hello"` and `str2 = "Maaz"`  concatenate `str1 + str2`   
2. `username = "Maaz\n"` and `print(username * 5)`   
3. `str1 = " abcd " ` and print("a" in str1)   
4. `str = "MaazMS"` and `print(str[0])` 
5. `str = "abcdef"` and `print(str[0 : 6])`  

### string method   
1. title : It is capital first letter of each word.  
2. casefold : It is convert upper letter to lower letter. 
3. count : It is use to count how many times repeat letter in string. 
4. find : find letter in string.  
5. capitalize : capital of first letter in word.  
6. format : It is use to replace value by {}.  
7. format_map : replace dictionary value.    
8. isalnum : It is check string contain only character or only digits without decimal then true otherwise false.  
9. isalpha : It return if string contain character if other then character then false   
10. isdecimal : It check Decimal return true other then false. Decimal  are those that can be used to form numbers by base 10 1.e 1 , 3, 5,etc.  
11. isidentifier : It check it is identifier or not.  

#### Example of string method   
1. `str = 'maaz shaikh'` and **str.title()**   
2. `str1 = "Maaz"` and **str2.casefold()**    
3. `str1 = "aa"` and ***str1.count('a')**  
4. `str = 'abcd'` and ***str.find('d')**  
5. `str = 'maaz shaikh'` and **str.capitalize()***  
6. `name = "Maaz"` and ***print("my name is {}".format(name))**  
7. `lunch = {"Food": "Pizza", "Drink": "Wine", "mobile" : "Mi"}` and **print("Lunch: {Food}, {Drink} {mobile}".format_map(lunch))***  
8. `a = "Fitness"`  or `a1 = "123"` and ***a.isalnum()**  
9. `b = "Fitness"`  and ***b.isalpha()**  
10. `c = "123"` and **c1.isdecimal()***  
11. `d1 = "_user_123"` and **d1.isidentifier()***  