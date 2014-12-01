#Tony K.
#25/11/2014
#Python Improvement Exercise



#Functions
import random

#Get Input from user
def input_details():
    table = int(input("Which times-table do you want to be tested on? "))
    return table

#Loop
def loop1(table):
    for questions in range(1,21):
        num1 = table
        num2 = random.randrange(2,13)
        total = num1 * num2
        UserAnswer = input(str(num1) + ' x ' + str(num2) + ' = ? ')
        UserAnswer = int(UserAnswer)
        if UserAnswer == total:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',total)
            print()
#main
def main():
    table = input_details()
    UserAnswer = loop1(table)
    print("Finished :) ")
