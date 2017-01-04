import random
import math
import os

user_plays = []
ai_plays = []

def getrand(min, max):
    return random.randint(min, max)

def make_board():
    board = [[],[],[]]
    for i in range(0, 3):
        board[i] += [['*'],['*'],['*']]
    return board

def getstep(board, user_plays, ai_plays):
    step = ai_plays[-1]
    xcoor = int(step[0])
    ycoor = int(step[2])
    choose = getrand(0, 1)
    if choose = 0:
        xcoor += 1
        ycoor += 1
        

def Print_board(board):
    count = 0
    for i in board:
        count += 1
        print(i, end="")
        print("\n")

def update(y, x, board, change):
    board[x][y] = change
    return board

def Playchance(board, usery, userx, computer, ai_plays, user_plays):
    ycoord = getrand(0, 2)
    xcoord = getrand(0, 2)
    ai_chan = str(xcoord)+','+str(ycoord)
    while ai_chan in user_plays or ai_chan in ai_plays:
        ycoord = getrand(0, 2)
        xcoord = getrand(0, 2)
        ai_chan = str(xcoord)+','+str(ycoord)
    ai_plays += [ai_chan, ]
    update(ycoord, xcoord, board, computer)

board = make_board()
Print_board(board)
char = input("Enter the charcacter you wish to use(choose x or 0) : ")
print("You will be using ", char)
if char.lower() == "x":
    computer = "0"
else:
    computer = "x"
print("The computer will be using " ,computer)
print("Your chance firs, use coordinates to refernace positions. The top left place is (1, 1)(y,x)")

while True:
    print("User_plays is ", user_plays)
    print("AI Plays is ", ai_plays)
    user_chance = input("Enter the coordinates")

    if user_chance in user_plays or user_chance in ai_plays:
        user_chance = input("Enter valid coordinates")

    user_plays += [user_chance, ]
    coord = []
    for i in user_chance:
        if i.isdigit():
            coord += [i, ]
    print(coord)
    board = update(int(coord[1]), int(coord[0]), board, char)
    os.system("clear")
    Playchance(board, int(coord[1]), int(coord[0]), computer, ai_plays, user_plays)
    Print_board(board)
