# define functions
def algorithm():
    validGrid = False
    while validGrid == False:
        thisGridSize = int(input("Please enter the size of the grid(max 20): "))
        if thisGridSize < 0:
            print("You have entered an invalid number ({0})".format(thisGridSize))
        if thisGridSize <= 20:
            validGrid = True
        else:
            print("The value entered is too big({0})".format(thisGridSize))
    return thisGridSize

def GetGridRow(rithm):
    # draws a single row using |_ for each square
    thisRow = '|_' * (rithm)
    # add closing | to row
    thisRow = thisRow + '|'
    return thisRow

def DisplayGrid(aGridSize, aRow):
    # display top of grid using _ as top of each square
    print(' _' * aGridSize)
    # display rows of |_| for each row
    for rowCount in range(aGridSize):
        print(aRow)

# main program
rithm = algorithm()
rowToDraw = GetGridRow(rithm)
DisplayGrid(rithm, rowToDraw)
