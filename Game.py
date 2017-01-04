import random
import math
import os
import platform
import time

def getrand(min, max):
    return random.randint(min, max)

def make_board():
    board = [[],[],[]]
    for i in range(0, 3):
        board[i] += [['*'],['*'],['*']]
    return board

def Print_board(board):
    count = 0
    for i in board:
        count += 1
        print(i, end="")
        print("\n")

def update(y, x, board, change):
    board[x][y] = change
    return board

def Playchance(board, usery, userx, computer):
    ycoord = getrand(0, 2)
    xcoord = getrand(0, 2)
    while xcoord == userx and ycoord == usery:
        ycoord = getrand(0, 2)
        xcoord = getrand(0, 2)
    update(ycoord, xcoord, board, computer)

def getplat():
    return platform.system()

platform = getplat()
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
    user_chance = input("Enter the coordinates")
    coord = []
    for i in user_chance:
        if i.isdigit():
            coord += [i, ]
    print(coord)
    board = update(int(coord[1]), int(coord[0]), board, char)
    if platform.lower() == 'windows':
        os.system("cls")
    else:
        os.system("clear")
    time.sleep(0.5)
    Playchance(board, int(coord[1]), int(coord[0]), computer)
    Print_board(board)
