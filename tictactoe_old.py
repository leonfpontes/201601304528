def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nVoce nao pode escolher essa casa. Tente denovo!")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nVoce nao pode escolher essa casa. Tente denovo!")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nEssa casa nao existe no tabuleiro. Tente denovo!")
                        continue
                except ValueError:
                   print("\nIsso nao eh um numero. Tente denovo!")
                   continue

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

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Jogador 1, escolha onde ira colocar o X")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Jogador 2, escolha onde ira colocar a O")
        p2()
        print()

    if input("Jogar de novo? (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()