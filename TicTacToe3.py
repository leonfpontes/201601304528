#Author: Vijay Nag
# A simple minimax based tic-tac-toe program
# TODO: alpha-beta pruning to improve running time

#!/usr/bin/python

import os, sys, time, string, copy

WIN=10
LOSE=-10

def max(a,b):
    return a if a > b else b

def min(a,b):
    return a if a < b else b

def GetScore(game):
    if IsGameOver(game, 'O'):
        return WIN, 'O'
    elif IsGameOver(game, 'X'):
        return LOSE, 'X'
    else:
        return 0, 0

def minimax(game, depth, maximizingplayer):

    score, choice = GetScore(game)
    if depth == 0 or score == WIN or score == LOSE:
        return score, game

    if maximizingplayer:
        best = LOSE
        best_child = None
        games = GeneratePossibleMoves(game, 'O')
        for child in games:
            v, move = minimax(child, depth-1, False)
            if v > best-1:
                best_child = child
                best = v
        return best, best_child
    else:
        best = WIN
        best_child = None
        games = GeneratePossibleMoves(game, 'X')
        for child in games:
            v, move = minimax(child, depth-1, True)
            if v <= best:
                best_child = child
                best = v
        return best, best_child

#Returns True if game has reached the
#final end state for the symbol choice
#Also if the match is draw
def IsGameOver(Gameboard, choice):

    #First row
    if Gameboard[0][0] == choice and \
       Gameboard[0][1] == choice and \
       Gameboard[0][2] == choice:
        return True

    #Second row
    if Gameboard[1][0] == choice and \
       Gameboard[1][1] == choice and \
       Gameboard[1][2] == choice:
        return True

    #Third row
    if Gameboard[2][0] == choice and \
       Gameboard[2][1] == choice and \
       Gameboard[2][2] == choice:
        return True

    #First column
    if Gameboard[0][0] == choice and \
       Gameboard[1][0] == choice and \
       Gameboard[2][0] == choice:
        return True

    #second column
    if Gameboard[0][1] == choice and \
       Gameboard[1][1] == choice and \
       Gameboard[2][1] == choice:
        return True

    #third column
    if Gameboard[0][2] == choice and \
       Gameboard[1][2] == choice and \
       Gameboard[2][2] == choice:
        return True

    #Diagnol
    if Gameboard[0][0] == choice and \
       Gameboard[1][1] == choice and \
       Gameboard[2][2] == choice:
        return True

    #Diagnol
    if Gameboard[0][2] == choice and \
       Gameboard[1][1] == choice and \
       Gameboard[2][0] == choice:
        return True

    return False

def CopyMove(dst, src):
    for row in range(3):
        for col in range(3):
            dst[row][col] = src[row][col]

def GeneratePossibleMoves(Gameboard, choice):
    list_of_moves = []

    for row in range(3):
        for col in range(3):
            if Gameboard[row][col] == '-':
                game = copy.deepcopy(Gameboard)
                game[row][col] = choice
                list_of_moves.append(game)
    return list_of_moves

def NextMove(Gameboard):
    score, game = minimax(Gameboard, 2, True)
    if (game == None):
        GameComplete(score, [])
    CopyMove(Gameboard, game)
    score, choice = GetScore(Gameboard)
    return score, 'xx'

def GameComplete(score, Gameboard):
    cont = True

    if Gameboard == []:
        print ('Game drawn!!!')
        cont = False
    elif score == LOSE:
        print ('Congratulations!!! You win :)')
        cont = False
    elif score == WIN:
        print ('You lose')
        cont = False

    if cont: return

    PrintGameBoard(Gameboard, clear=False)
    print "Press y to continue; any other key to exit"
    y = raw_input()

    if y == 'y':
        Initialize(Gameboard)
        PrintBanner()
    else:
        sys.exit(0)

def PrintGameBoard(Gameboard, clear = True):
    if clear:
       os.system("clear")
    for rows in Gameboard:
        for cols in rows:
            print cols,
        print "\n"

def readChoice(Gameboard):
    while True:
        try:
            line = sys.stdin.readline()
            x, y = string.split(line[:-1])
            x, y = int(x)-1, int(y)-1
            return x,y
        except:
            return -1, -1

def PrintBanner():
    os.system("clear")
    print "Welcome to Tic-Tac-Toe"
    print "Players choice is X and my choice is O"
    time.sleep(1)

def Initialize(Gameboard):
    for r in range(3):
        for c in range(3):
            Gameboard[r][c] = '-'

def main():

    Gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
    PrintBanner()
    while True:

        PrintGameBoard(Gameboard)
        print "Enter (row, column)\n"
        row,col = readChoice(Gameboard)
        if (row, col) == (-1,-1):
            continue

        if Gameboard[row][col] != '-':
            print "Choice already filled"
            continue
        Gameboard[row][col] = 'X'

        score, choice = GetScore(Gameboard)
        GameComplete(score, Gameboard)

        score, choice = NextMove(Gameboard)
        GameComplete(score, Gameboard)

if __name__ == "__main__":
    main()