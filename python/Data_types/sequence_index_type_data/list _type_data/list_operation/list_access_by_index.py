# List index start from zero
# list index -1 for right to left move
_string = ['a', 'b', 'c', 'd', 'e', 'f']
print(" index access from left to right")
print("index of _string [0] ", _string[0])
print("index of _string [1] ", _string[1])
print("index of _string [2] ", _string[2])
print("index of _string [3] ", _string[3])
print("index of _string [4] ", _string[4])
print("index of _string [5] ", _string[5])

print(" index access from right to left  ")

print("index of _string [-1] ", _string[-1])
print("index of _string [-2] ", _string[-2])
print("index of _string [-3] ", _string[-3])
print("index of _string [-4] ", _string[-4])
print("index of _string [-5] ", _string[-5])
print("index of _string [-6] ", _string[-6])

print(" start_index (first element) : end element (count start from 1 not zero)")
print("index of _string [  : 1]  ", _string[  : 1]) # ['a']
print("index of _string [0 : 1]  ", _string[0 : 1]) # ['a']
print("index of _string [0 : 6]  ", _string[0 : 6]) # ['a', 'b', 'c', 'd', 'e', 'f']
print("index of _string [2 : 6]  ", _string[2 : 6])

print(" start_index : end element : number of step")
print("index of _string [0: 6 : 1]  ", _string[0: 6 : 1]) # ['a', 'b', 'c', 'd', 'e', 'f']
print("index of _string [0: 6 : 2]  ", _string[0: 6 : 2]) #  ['a', 'c', 'e']

print("not defind start index : not define last index")
print("not defind start index : not define last index", _string[:])

print("check list element return true and false")
print("check a in list _string ",'a' in _string)
print("check z in list _string ",'z' in _string)

print("+ , * operator use in list ")
print("use + operator in list to add element in list but not insert permanently in list ")
print(" _string 'g' add in list  ", _string + ['g'])
print("1 add in list  _string  ", [1] + _string )


print("use * operator in list to double or triple element in list based of operand ")
print(" _string * 2  is equal to ", _string * 2)