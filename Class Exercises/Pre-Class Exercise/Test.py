#Tony K.
#25/11/2014
#Python Improvement Exercise



#Functions

#Get Input from user
def testTable():
    number = int(input("Which times-table do you want to be tested on? "))
    return number

#Loop
def loop(number):
    import random
    for questions in range(1,21):
       Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)
    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()

def main():
    test = testTable()
    test1 = loop(number)

    
