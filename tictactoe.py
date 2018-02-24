from random import *

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def choose_number():
        bStop = False
        token = 'X'
        end = False
        while not bStop:
            a = randint(0,8)
            try:
                if board[a] == "X" or board[a] == "O":
                    bStop = False
                else:
                    if token == 'X':
                        board[a] = 'X'
                        token = 'O'
                    else:
                        board[a] = 'O'
                        token = 'X'
                    bStop = False
                    
                end = check_board()
                if end == True:
                    break
            except ValueError:
                print("\nERRO GERAL NO CHOOSE_NUMBER")
                
        draw()

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Payer 1 Ganhou!\n")
                print("Parabens!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 2 Ganhou!\n")
                print("Parabens!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Deu velha =/ n")
                return True

    choose_number()

tic_tac_toe()