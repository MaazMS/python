# you can give any condtion we use `#`.

# open the file for writing
f = open("multiple_strings.txt", "w")
print("Enter the thext (if type # on prompt the it is stop. )")
txt = ''
while(txt !='#'):
    txt = input()
    f.write(txt+"\n")
f.close()