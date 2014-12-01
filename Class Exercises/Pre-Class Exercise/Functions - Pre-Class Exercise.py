# functions improvement exercise
# times-table tester
import random

# main program
print("Times-table tester")
print()
testTable = input("Which times-table do you want to be tested on? ")
testTable = int(testTable)
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
#re-write
print("Times-table tester")
print()
testTable = int(input("Which times-table do you want to be tested on: "))
for questions in range(1,21):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = int(input("{0:<2}x {1:<2}= ".format(Num1,Num2)))
    if UserAnswer == Ans:
        print("Well done, you got the correct answer!")
        print()
    else:
        print("Sorry, you got the answer wrong. The correct answer is{0}".format(Ans))
        print()

