import getpass

def password():


    username = input('Enter user name username: ')
    password = getpass.getpass('Enter user password: ')
    print("check password",password)


if __name__ == '__main__':
    password()

# This program run through terminal
# (venv) maaz@maaz-Lenovo-G50-70:~/maaz/ws/python/python_programs/getpass_for_password$ python3 pass_without_echoing.py
# Enter user name username: Maaz
# Enter user password:
# check password HelloMaaz
