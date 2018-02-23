import sys
import time
import getopt

if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hf:b:v", ["first=" , "board=", "verbose="])
        for opt, arg, in opts:
            if opt == '-h':
                print("%s -f x -b ____x____" %(__file__))
                sys.exit()
            elif opt in ("-v", "--verbose"):
                print board(board)
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board")
    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))