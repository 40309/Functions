#Tony K.
#08/12/2014
#Funcions Spotcheck Part 1

def loop():
    password_check = "False"
    while password_check == "False":
        user_input = input("Please enter your password: ")
        length = len(user_input)
        if length < 8:
            print("Password is too Short")
        elif length > 16:
            print("Password is too long")
        else:
            password_check = "True"
            print("Password Accepted")
    return user_input

def main():
    calling = loop()
    
