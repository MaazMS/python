int_number = 10
float_number = 10.9
devision_number  = 3 / 2
complex_number = 1 + 2j
int_number_in_string = "123"
float_number_in_string = "123.9"

# convert integer  to float and complex

int_to_float = float(int_number)
int_to_complex = complex(int_number)


print('int_to_float', int_to_float)
print('int_to_complex', int_to_complex)

# convert float to int and complex

float_to_int = int(float_number)
float_to_complex = complex(float_number)

print('float_to_int', float_to_int)
print('float_to_complex', float_to_complex)

# convert division number to int, float and complex

division_num_to_int = int(devision_number)
division_num_to_float = float(devision_number)
division_num_to_complex = complex(devision_number)

print('devision_number', devision_number)
print('division_num_to_int', division_num_to_int)
print('division_num_to_float', division_num_to_float)
print('division_num_to_complex', division_num_to_complex)


# convert complex to int and float
#  TypeError: can't convert complex to float
# complex_to_int = int(complex_number)
# complex_to_float = float(complex_number)

# convert string to int and float

string_to_int = int(int_number_in_string)
string_to_float = float(float_number_in_string)
print("string_to_int",string_to_int)
print("string_to_int",string_to_float)


#  number_in_string = "123"
# ValueError: invalid literal for int() with base 10: '123f'