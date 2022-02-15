one =" "
two =" "
thr =" "
fou = " "
fiv =" "
six =" "
sev =" "
eig =" "
nin =" "
game = True


def is_empty():
    global game
    if any([one==" ", two==" ", thr==" ", fou==" ", fiv==" ", six==" ", sev==" ", eig==" ", nin==" "]):
        pass
    else:
        print("Draw!")
        game = False



def player1():
    global game, one, two, thr, fou, fiv, six, sev, eig, nin
    player_1 = input("player 1: ")
    if player_1 == "1":
        if one == " ":
            one = "X"
        else:
            print("position already occupy")
            player1()
    if player_1 == "2":
        if two == " ":
            two = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "3":
        if thr == " ":
            thr = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "4":
        if fou == " ":
            fou = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "5":
        if fiv == " ":
            fiv = "X"
        else:
            print("position already occupy")
            player1()
    if player_1 == "6":
        if six == " ":
            six = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "7":
        if sev == " ":
            sev = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "8":
        if eig == " ":
            eig = "X"
        else:
            print("position already occupy")
            player1()

    if player_1 == "9":
        if nin == " ":
            nin = "X"
        else:
            print("position already occupy")
            player1()
    print(
        f"""
                       |       |
                  {one}    |   {two}   |  {thr}
               -------------------------
                       |       |
                  {fou}    |   {fiv}   | {six}
               -------------------------
                       |       |
                  {sev}    | {eig}     | {nin}
                   """
    )
    if all([one == "X", two == "X", thr == "X"]) or all([fou == "X", fiv == "X", six == "X"]) or all(
            [sev == "X", eig == "X", nin == "X"]) or all([one == "X", fou == "X", sev == "X"]) or all(
        [two == "X", fiv == "X", eig == "X"]) or all([thr == "X", six == "X", nin == "X"]) or all(
        [one == "X", fiv == "X", nin == "X"]) or all([thr == "X", fiv == "X", sev == "X"]):
        print("Player_1 Win!")

        game = False

def player2():
    global game, one, two, thr, fou, fiv, six, sev, eig, nin
    player_2 = input("player 2: ")
    if player_2 == "1":
        if one == " ":
            one = "O"
        else:
            print("position already occupy")
            player2()
    if player_2 == "2":
        if two == " ":
            two = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "3":
        if thr == " ":
            thr = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "4":
        if fou == " ":
            fou = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "5":
        if fiv == " ":
            fiv = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "6":
        if six == " ":
            six = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "7":
        if sev == " ":
            sev = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "8":
        if eig == " ":
            eig = "O"
        else:
            print("position already occupy")
            player2()

    if player_2 == "9":
        if nin == " ":
            nin = "O"
        else:
            print("position already occupy")
            player2()
    print(
        f"""
                    |       |
               {one}    |   {two}   |  {thr}
            -------------------------
                    |       |
               {fou}    |   {fiv}   | {six}
            -------------------------
                    |       |
               {sev}    | {eig}     | {nin}
        """
    )
    if all([one == "O", two == "O", thr == "O"]) or all([fou == "O", fiv == "O", six == "O"]) or all(
            [sev == "O", eig == "O", nin == "O"]) or all([one == "O", fou == "O", sev == "O"]) or all(
            [two == "O", fiv == "O", eig == "O"]) or all([thr == "O", six == "O", nin == "O"]) or all(
            [one == "O", fiv == "O", nin == "O"]) or all([thr == "O", fiv == "O", sev == "O"]):
        print("player_2 Win!")
        game = False




def tic_tac():
    global game
    while game:
        player1()
        is_empty()
        if game ==False:
            break
        player2()

        is_empty()

tic_tac()