
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
movemade = False
win = False

print ("Let's play Tic Tac Toe!")
print ( "|".join(row1))
print ( "|".join(row2))
print ( "|".join(row3))
for turn in range(1, 10):
    
    if (turn % 2) == 1:
        piece = "X"
    else:
        piece = "O"
    print ( " It's currently turn number " , turn , "! ")
    if (turn % 2) == 1:
        print (" Player 1’s Turn! (X) Make your move!")
    else:
        print (" Player 2’s Turn! (O) Make your move!")
    while movemade == False:
        moverow = int (input ("Enter Row:")) 
        movecol = int (input ("Enter Column:")) - 1
        if moverow == 1:
            if row1[movecol] == " ":
                row1[movecol] = piece
                movemade = True
            else:
                print ("That spot is taken. Try another one.")
        if moverow == 2:
            if row2[movecol] == " ":
                    row2[movecol] = piece
                    movemade = True
            else:
                print ("That spot is taken. Try another one.")
        if moverow == 3:
            if row3[movecol] == " ":
                row3[movecol] = piece
                movemade = True
            else:
                print ("That spot is taken. Try another one.")
    print ( "|".join(row1))
    print ( "|".join(row2))
    print ( "|".join(row3))
    
    if row1[0] == row1[1] == row1[2] != " ":
        if row1[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row1[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row2[0] == row2[1] == row2[2]!= " ":
        if row2[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row2[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row3[0] == row3[1] == row3[2]!= " ":
        if row3[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row3[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row1[0] == row2[0] == row3[0]!= " ":
        if row1[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row1[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row1[1] == row2[1] == row3[1]!= " ":
        if row1[1] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row1[1] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row1[2] == row2[2] == row3[2]!= " ":
        if row1[2] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row1[2] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row1[0] == row2[1] == row3[2]!= " ":
        if row1[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row1[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    if row3[0] == row2[1] == row1[2]!= " ":
        if row3[0] == "X":
            print ("Player 1 (X) Wins!")
            win = True
            break
        if row3[0] == "O":
            print ("Player 2 (O) Wins!")
            win = True
            break
    else:
        movemade = False
print ("The game has ended!")
if win == False:
    print ("Looks like there's a tie! You should try again!")
        
