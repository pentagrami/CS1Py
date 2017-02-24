from random import randint , randrange , sample
playagain = True
def board (x):
    for i in range (0,3):
        print ( "|".join(x[i]))
def wincheck (win , x , mark , current):
    wincounter = 0
    for i in range (0 , 3 ):
        for l in range (0 , 3):
            if x[i][l] == mark:
                   wincounter = wincounter + 1
            if wincounter == 3:
                print ("Player" , current , "(" , mark , ") wins!")
                win = True
                wincounter =0
            else:
                wincounter = 0
                        
    for i in range (0 , 3):
        for l in range (0 , 3):
            if x[l][i] == mark:
               wincounter = wincounter + 1
        if wincounter == 3:
            print ("Player" , current , "(" , mark , ") wins!")
            win = True
            wincounter =0       
        else:
            wincounter = 0
                
    if x[0][0] == x[1][1] == x[2][2]== mark or x[2][0] == x[1][1] == x[0][2]== mark:
        print ("Player" , current , "(" , mark , ") wins!")
        win = True
    return win

        
while playagain == True:
    row = [[" "," "," "],[" "," "," "],[" "," "," "]]
    counter = 0
    wincounter = 0
    compcounter = 0
    player = 0
    movemade = False
    win = False
    winner = 0
    legal = False
    moveburned1 = False
    moveburned2 = False
    playerpiece = "undef"

    print ("Let's play Tic Tac Toe!")
    board (row)
    while legal == False:
        playerchoiceprelim = (input("Do you want to go first or second? (Enter 1 or 2): "))
        if playerchoiceprelim in ["1","2"]:
            playerchoice = int (playerchoiceprelim)
            legal = True
        else:
            print ("Please enter only 1 or 2!")
    legal = False


    for turn in range(1, 10):
        print ( " It's currently turn number " , turn , "! ")
        if (turn % 2) == 1:

            piece = "X"
            player = 1
            print (" Player 1’s Turn! (X)")

        else:

            piece = "O"
            player = 2
            print (" Player 2’s Turn! (O)")
            
        if player == playerchoice:
            playerpiece = piece
            print (" It's your turn! Make your move!")

            while movemade == False:
                while legal == False:
                    moverowprelim = input ("Enter Row (1-3): ")
                    movecolprelim = input ("Enter Column (1-3): ")
                    if (moverowprelim in ["1","2","3"]) and (movecolprelim in ["1","2","3"]):
                        moverow = int (moverowprelim) - 1
                        movecol = int (movecolprelim) - 1
                        legal = True
                        
                    else:
                        print ("Please enter only whole numbers 1 through 3")
                legal = False

                

                if row[moverow][movecol] == " ":

                    row[moverow][movecol] = piece

                    movemade = True

                else:

                    print ("That spot is taken. Try another one.")

        else:
            print (" It's the computer's turn!")
            
            randone = randrange(0,3,2)
            randtwo = randrange (0,3,2)
          
            
            while movemade == False:
                if playerchoice == 1 and row[1][1] == " ":
                    row[1][1] = piece
                    movemade = True
                elif playerchoice == 1 and row [1][1] == playerpiece and turn == 2:
                    row [0][0] = piece
                    movemade = True
                elif row[2][2] == piece and row[0][0] == piece and row[1][1] == " ":
                    row[1][1] = piece
                    movemade = True
                elif row[0][0] == playerpiece and row[2][2] == playerpiece and row[1][1] == piece and row [0][1] == " ":
                    row[0][1] = piece
                    movemade = True
                elif row[0][2] == playerpiece and row[2][0] == playerpiece and row[1][1] == piece and row[2][1] == " ":
                    row[2][1] = piece
                    movemade = True
                elif row[1][1] == playerpiece and row[2][0] == playerpiece and row[0][2] == piece and row[0][0] == " ":
                    row[0][0] = piece
                    movemade = True
                elif row[2][2] == piece and row[1][1] == piece and row[0][0] == " ":
                    row[0][0] = piece
                    movemade = True
                elif row[1][1] == piece and row[0][0] == piece and row[2][2] == " ":
                    row[2][2] = piece
                    movemade = True
                elif row[0][2] == piece and row[2][0] == piece and row[1][1] == " ":
                    row[1][1] = piece
                    movemade = True
                elif row[0][2] == piece and row[1][1] == piece and row[2][0] == " ":
                    row[2][0] = piece
                    movemade = True
                elif row[1][1] == piece and row[2][0] == piece and row[0][2] == " ":
                    row[0][2] = piece
                    movemade = True
                elif row[2][2] == playerpiece and row[0][0] == playerpiece and row[1][1] == " ":
                    row[1][1] = piece
                    movemade = True
                elif row[2][2] == playerpiece and row[1][1] == playerpiece and row[0][0] == " ":
                    row[0][0] = piece
                    movemade = True
                elif row[1][1] == playerpiece and row[0][0] == playerpiece and row[2][2] == " ":
                    row[2][2] = piece
                    movemade = True
                elif row[0][2] == playerpiece and row[2][0] == playerpiece and row[1][1] == " ":
                    row[1][1] = piece
                    movemade = True
                elif row[0][2] == playerpiece and row[1][1] == playerpiece and row[2][0] == " ":
                    row[2][0] = piece
                    movemade = True
                elif row[1][1] == playerpiece and row[2][0] == playerpiece and row[0][2] == " ":
                    row[0][2] = piece
                    movemade = True
                elif turn > 2 and row[1][1] == " ":
                    row [1][1] = piece
                    movemade = True
                else:
                    complete = False
                    while complete == False:
                        counter = 0
                        compcounter = 0
                        for i in range (0 , 3):
                            if complete == False:
                                compcounter = 0
                                for l in range (0 , 3):
                                    if row[i][l] == piece:
                                        compcounter = compcounter + 1
                                if compcounter == 2:
                                    for p in range (0 , 3):
                                        if row[i][p] == " ":
                                            row[i][p] = piece
                                            movemade = True
                                            complete = True
                                            compcounter = 0
                        for i in range (0,3):
                            compcounter = 0
                            if complete == False:
                                for l in range (0 , 3):
                                    if row[l][i] == piece:
                                        compcounter = compcounter + 1
                                if compcounter == 2:
                                    for p in range (0 , 3):
                                        if row[p][i] == " ":
                                            row[p][i] = piece
                                            movemade = True
                                            complete = True
                                            compcounter = 0
                                
                        for i in range (0,3):                                                        
                            if complete == False:
                                counter =0
                                for l in range (0 , 3):             
                                    if row[i][l] == playerpiece:
                                        counter = counter + 1
                                if counter == 2:
                                    for p in range (0 , 3):
                                        if row[i][p] == " ":
                                            row[i][p] = piece
                                            movemade = True
                                            complete = True
                                            counter = 0
                                                        
                        for i in range (0,3):
                            if complete == False:
                                counter = 0
                                for l in range (0 , 3):
                                    if row[l][i] == playerpiece:
                                        counter = counter + 1
                                if counter == 2:
                                    for p in range (0 , 3):
                                        if row[p][i] == " ":
                                            row[p][i] = piece
                                            movemade = True
                                            complete = True
                                            counter = 0
                                                        

                                
                        if complete == False:
                            while legal == False:
                                randrow = randint(0,2)
                                randcol = randint(0,2)
                                if row[randrow][randcol] == " ":
                                    row[randrow][randcol] = piece
                                    movemade = True
                                    complete = True
                                    legal = True
                            legal = False
                                        
        board(row)
        win = wincheck (win , row , piece , player)
        if win == True:
            winner = player
            break
        else:
            movemade = False

    print ("The game has ended!")

    if win == False:

        print ("Looks like there's a tie! You should try again!")
    else:
        if winner == playerchoice:
            print ("You beat the computer!")
        else:
            print ("The computer has won! Try again!")
    while legal == False:
        ask = input ("So, do you want to play again? (y/n) ")
        if ask in ["y","n"]:
            if ask == "n":
                playagain = False
            legal = True
        else:
            print ("Please enter only 'y' or 'n'")

        
