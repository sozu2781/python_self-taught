def hangman(word):
    wrong=0
    stages=["",
            "_______       ",
            "|      |      ",
            "|      o      ",
            "|     /|1  ",
            "|     /し  ",
            "|        ",
            "L_"
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Welcome to Hangman!")
    while wrong<len(stages) -1:
        print("\n")
        msg="guess 1 letter"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose!\n answer is {}.".format(word))


