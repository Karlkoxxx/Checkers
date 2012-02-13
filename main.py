# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106
# These 
# Main class runs the game
from board import *
from minmax import *

# Setup variables
width = 6
height = 6
maxDepth = 5

# define auxilary methods
# Gets the move from the User
def getUserMove(b):
    statement1 = "Select one of your tokens eg. " + chr(b.whitelist[0][0]+97) + str(b.whitelist[0][1])
    print(statement1)
    while True: # Loop until proper input
        move = []
        move = raw_input().lower().split()
        if not(len(move) == 2):
            print "That is not a valid move, try again.", statement1
            continue
        moveFromTup = (int(move[0][1]), ord(move[0][0]) - 97)
        moveToTup = (int(move[1][1]), ord(move[1][0]) - 97)
        if moveFromTup in b.blacklist:
            print "You do not own that piece, that is a black piece.", statement1
            continue
        elif not (moveFromTup in b.whitelist):
            print "You do not own", moveFromTup, "please select one of.", b.whitelist
            continue
        break
    move = (moveFromTup, moveToTup, -1)
    return move

### MAIN PROGRAM ###
# Setup the board
#print("Input board width")
#width = int(raw_input())
#print("Input board height")
#height = int(raw_input())
#print("Enter a number between 0 and 7 for the difficulty setting. 7 = hardest "
#    + "0 = dead easy:")
#maxDepth = int(raw_input())

b = board(width, height)
b.printBoard()
print("Welcome to checkers. Type help at any time for additional information")

# Main game loop
while b.gameWon == -1:
    # First it is the users turn
    userMove = getUserMove(b)
    b.moveWhite(*userMove)
    # Then it is the computers turn
    temp = minMax(b, maxDepth)
    b = temp[0]
    print "**********COMPUTER MOVE**********"
    print "best move was", temp[1]
    b.printBoard()
    if b.gameWon == b.WHITE:
        print "White Wins\nGame Over"
        break
    elif b.gameWon == b.BLACK:
        print "Black Wins\nGame Over"
        break
