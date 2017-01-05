import random
import math
import os
import platform
import time

user_plays = []
ai_plays = []
possible = []

def getrand(min, max):
    return random.randint(min, max)
#Initialize the board
def make_board():
    board = [[],[],[]]
    for i in range(0, 3):
        board[i] += [['*'],['*'],['*']]
    return board
#Initialize the possible variable
def init_possible(board, possible):
    u = 0
    possible = possible
    while u < len(board):
        y = 0
        while y < len(board[u]):
            coor =str(u) + ',' + str(y)
            possible += [coor, ]
            y += 1
        u += 1
    return possible
#Print the board
def Print_board(board):
    count = 0
    for i in board:
        count += 1
        print(i, end="")
        print("\n")
#Get empty positions from the current game instance
def getempty(possible, ui ,ai):
    empty = []
    for i in possible:
        if i not in ui and i not in ai:
            empty += [i, ]
    return empty
#Update the board
def update(y, x, board, change):
    board[x][y] = change
    return board
#Get the char at a position
def getcharat(board, coord):
	xcoord = int(coord[0])
	ycoord = int(coord[2])
	return board[xcoord][ycoord]
# function that plays a  chance
def Playchance(board, computer, coord, ai_plays):
    xcoord = int(coord[0])
    ycoord = int(coord[2])
    #  usery, userx, computer, ai_plays, user_plays
    # ycoord = getrand(0, 2)
    # xcoord = getrand(0, 2)
    ai_chan = str(xcoord)+','+str(ycoord)
    # while ai_chan in user_plays or ai_chan in ai_plays:
    #     ycoord = getrand(0, 2)
    #     xcoord = getrand(0, 2)
    #     ai_chan = str(xcoord)+','+str(ycoord)
    ai_plays += [ai_chan, ]
    update(ycoord, xcoord, board, computer)
#Get the platform of the computer
def getplat():
    return platform.system()

#Get element just up
def up(board, coord):
    xcoord = int(coord[0]) - 1
    ycoord = int(coord[2])
    if xcoord < 0 or ycoord < 0:
        return "End"
    else:
        return board[xcoord][ycoord]

#Get element just above
def down(board, coord):
    xcoord = int(coord[0]) + 1
    ycoord = int(coord[2])
    if xcoord > 2 or ycoord > 2:
        return "End"
    else:
        return board[xcoord][ycoord]

#Get element just right
def right(board, coord):
    xcoord = int(coord[0])
    ycoord = int(coord[2]) + 1
    if xcoord > 2 or ycoord > 2:
        return "End"
    else:
        return board[xcoord][ycoord]

#Get element just left
def left(board, coord):
    xcoord = int(coord[0])
    ycoord = int(coord[2]) - 1
    if xcoord < 0 or ycoord < 0:
        return "End"
    else:
        return board[xcoord][ycoord]

#Get element diagonaly right
def dright(board, coord):
    xcoord = int(coord[0]) + 1
    ycoord = int(coord[2]) + 1
    if xcoord > 2 or ycoord > 2:
        xcoord -= 2
        if ycoord >2:
            return "End"
        else:
            return board[xcoord][ycoord]
    else:
        return board[xcoord][ycoord]

#Get element diagonaly left
def dleft(board, coord):
    xcoord = int(coord[0]) - 1
    ycoord = int(coord[2]) - 1
    if xcoord < 0:
        xcoord += 2
        if ycoord <0 or xcoord < 0:
            return "End"
        else:
            return board[xcoord][ycoord]
    else:
        return board[xcoord][ycoord]

def getsurrouunding(i, board):
            coor = i
            xoor = int(i[0])
            ycoor = int(i[2])
            uper = up(board, coor)
            downer = down(board, coor)
            righter = right(board, coor)
            lefter = left(board, coor)
            drighter = dright(board, coor)
            dlefter = dleft(board, coor)
            surrounding = [uper,  righter, downer, lefter, drighter, dlefter]
            return surrounding
#Get the next best step
def getstep(board,  empty, char):
    best = empty[getrand(0, len(empty)-1)]
    highest = 0
    for i in empty:
        counter = 0
        surrounding = getsurrouunding(i, board)
        for k in surrounding:
            if k == char:
                counter += 1
        if counter > highest:
            highest = counter
            best = i
    return best
#Evaluate board for winners
def evaluate(board, user_char, computer_char, possible):
	cwin = False
	uwin = False
	y = 0
	while y < len(possible):
		coord = possible[y]
		ycoord = int(possible[y][0])
		xcoord = int(possible[y][2])
		surround = getsurrouunding(coord, board)
		charat = getcharat(board, coord)
		print("Coord is ", coord)
		print("Surround is ", surround)
		print("Charat is ", charat)
		y += 1
		if "*" in charat:
			continue
		else:
			if surround[0] == charat and surround[2] == charat:
				if charat == user_char:
					uwin = True
				elif charat == computer_char:
					cwin = True
				break
			if surround[4] == charat and surround[5] == charat:
				if charat == user_char:
					uwin = True
				elif charat == computer_char:
					cwin = True
				break
			if surround[1] == charat and surround[3] == charat:
				if charat == user_char:
					uwin = True
				elif charat == computer_char:
					cwin = True
				break
	return [uwin, cwin]

#Functions over the rest of the code calling the functions is below
platform = getplat()
board = make_board()
possible = init_possible(board, possible)
Print_board(board)
char = input("Enter the charcacter you wish to use(choose x or 0) : ")
print("You will be using ", char)
if char.lower() == "x":
    computer = "0"
else:
    computer = "x"
print("The computer will be using " ,computer)
print("Your chance firs, use coordinates to refernace positions. The top left place is (0, 0) -> (y,x)")
count = 0
while True:
    user_chance = input("Enter the coordinates")
    coord = []

    if user_chance in user_plays or user_chance in ai_plays:
        user_chance = input("Enter valid coordinates")

    user_plays += [user_chance, ]
    
    print(dright(board, user_plays[count]))
    empty = getempty(possible, user_plays, ai_plays)
    print("Empty is ", empty)
    print("Best step is ", getstep(board, empty, char))
    print("User_plays is ", user_plays)
    print("AI Plays is ", ai_plays)
    time.sleep(2)
    for i in user_chance:
        if i.isdigit():
            coord += [i, ]

    print(coord)
    empty = getempty(possible, user_plays, ai_plays)
    board = update(int(coord[1]), int(coord[0]), board, char)
    print("Char at is", getcharat(board, user_chance))
    time.sleep(2)
    if platform.lower() == 'windows':
        os.system("cls")
    else:
        os.system("clear")
    bstep = getstep(board, empty,char)
    Playchance(board, computer, bstep, ai_plays)
    # Playchance(board, int(coord[1]), int(coord[0]), computer, ai_plays, user_plays)
    Print_board(board)
    Ans = evaluate(board,char, computer, possible)
    if Ans[0] == True:
    	print("User won!!")
    	break
    elif Ans[1] == True:
    	print("The AI won!!")
    	break
    count += 1
