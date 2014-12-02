#Tony K. & Hamza
#01/12/2014
#Pre-Class Execise-Part2


#functions

def input_details():
    first_name = input("Please enter your First Name: ")
    last_name = input("Please enter yout last Name: ")
    gender = input("Please enter your gender: ")
    house_number = input("Please enter your house number/name: ")
    street_name = input("Please enter your street name: ")
    town = input("PLease enter your town name: ")
    post_code = input("Please enter your post code: ")
    post_code = post_code.upper()

    return first_name,last_name,gender,house_number,street_name,town,post_code

def title(gender):
    name_title = gender.upper()
    name_title = name_title[0]
    if name_title == "M":
        name_title = "Mr"
    elif name_title == "G":
        name_title = "Mrs"
    else:
        name_title = "Mx"
    return name_title

def display_details(name_title,first_name,last_name):
    print("Welcome {0}.{1} {2}, to Long Road Bank".format(name_title,first_name,last_name))

#main program
def main():
    print("We will have to ask you a few details.")
    details = input_details()
    if_statement = title(gender)
    display = display_details(name_title,first_name,last_name)
