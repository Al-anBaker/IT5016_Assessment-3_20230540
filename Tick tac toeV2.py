#By Alan Baker 2023 Mar 14
#Updated 8 Sept 2025

#Empty Squares
emty = "e"
#Player One Chooses what letter they would like
pl1 = input("Player One: Please input your letter or number you want to use: ")
#if it = emty they are asked to use a diffrent letter
if pl1 == emty:
    pl1 = input("Player One: Choose a diffrent letter: ")
#Player Two chooses what letter they would like
pl2 = input("Player Two: Please input your letter or number you want to use: ")
#if its equal to emty or player one's option they are propmeted to choose again
if (pl2 == emty) or (pl2 == pl1):
    pl2 = input("Player Two: Please choose a diffrent letter: ")
#Whose Turn is it?
turn = 0
#Is the gameover
gameover = False
#the list that makes the game board
game_board =  [emty,emty,emty,
              emty,emty,emty,
              emty,emty,emty]



#This Fuction draws the game board
def draw_game():
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")

#check_rows looks through the rows and sees if there is a win
#if there is a win it sets gameover to be true
def check_rows():
    row_1 = game_board[0] == game_board[1] == game_board[2] != emty
    row_2 = game_board[3] == game_board[4] == game_board[5] != emty
    row_3 = game_board[6] == game_board[7] == game_board[8] != emty
    if row_1 or row_2 or row_3:
        global gameover
        gameover = True
        win_check()
#check_collums looks through the collums and sees if there is a win
#if there is a win it sets gameover to be true
def check_collums():
    collum_1 = game_board[0] == game_board[3] == game_board[6] != emty
    collum_2 = game_board[1] == game_board[4] == game_board[7] != emty
    collum_3 = game_board[2] == game_board[5] == game_board[8] != emty
    if collum_1 or collum_2 or collum_3:
        global gameover
        gameover = True
        win_check()
#check_diags looks through the diagonals and sees if there is a win
#if there is a win it sets gameover to be true
def check_diags():
    diag_1 = game_board[0] == game_board[4] == game_board[8] != emty
    diag_2 = game_board[2] == game_board[4] == game_board[6] != emty
    if diag_1 or diag_2:
        global gameover
        gameover = True
        win_check()
        pass
def check_tie():
    global turn
    global gameover
    if emty not in game_board:
        turn = 3
        gameover = True
        win_check()
#game_over ends the game based on who wins
def game_over():
    global turn
    #turn 1 is player ones win
    if turn == 1:
        #draw_game here shows the last winning move
        draw_game()
        print("Player One Wins")
        print("Game Over!")
        play_again()
    #turn 2 is playe twos win
    elif turn == 2:
        #draw_game here shows the last winning move
        draw_game()
        print('Player Two Wins')
        print("Game Over!")
        play_again()
    elif turn == 3:
        #draw_game here shows the last move
        draw_game()
        print("Tie")
        print("Game Over!")
        play_again()
        
def win_check():
    global gameover
    if gameover == True:
        game_over()
    else:
        pass
    
    
#checks run every check function to see if a win condition has been achived
def checks():
    check_rows()
    check_collums()
    check_diags()
    check_tie()
#game_loop is the main game data and programming core
def game_loop():
    global turn
    #draw_game here draws the inital game state at the start of the game
    draw_game()
    player_one()
    #checks then goes through and checks if there is any winning condition if so it will end the game if not it will continue     
    checks()
    #this draws the turn just made
    draw_game()
    player_two()
    #checks then goes through and checks if there is any winning condition if so it will end the game if not it will continue
    checks()
    
    #this loops the game again and sends it to player one's turn
    game_loop()
    
#this resets the game after a win or tie condition happens
#it resets all the varibles back to their default state and asks for new letters 
def play_again():
    global emty
    global pl1
    global pl2
    global turn
    global gameover
    global game_board
    emty = "e"
    #Player One Chooses what letter they would like
    pl1 = input("Player One: Please input your letter or number you want to use: ")
    #if it = emty they are asked to use a diffrent letter
    if pl1 == emty:
        pl1 = input("Player One: Choose a diffrent letter: ")
#   Player Two chooses what letter they would like
    pl2 = input("Player Two: Please input your letter or number you want to use: ")
#   if its equal to emty or player one's option they are propmeted to choose again
    if (pl2 == emty) or (pl2 == pl1):
        pl2 = input("Player Two: Please choose a diffrent letter: ")
    #Whose Turn is it?
    turn = 0
    #Is the gameover
    gameover = False
#the list that makes the game board
    game_board =  [emty,emty,emty,
                emty,emty,emty,
                emty,emty,emty]
#this is the inital game start
def player_one():
    global turn
    #this is Player One's turn, userturn is a user input they can select an number between 0 and 8
    userturn = int(input("Player One: Please select a number 1 to 9: "))
    userturn = userturn - 1
    #this sets the winning turn players number incase there is a win
    turn = 1
    #this checks if the user input is in the requred values
    if userturn > 8 or userturn < 0:
        #if not it give this message and prompts the player to make another selection
        print("Selection is not 1-9")
        player_one()
    else:
        #else it checks if the spot is avalable is so it places their square down
        if game_board[userturn] == emty:
            game_board[userturn] = pl1
        else:
            #if not it prints this and prompts the player again
            print("Spot is Taken")
            player_one()

def player_two():
    global turn
    #this is Player Two's turn, userturn is a user input they can select an number between 1 and 9
    userturn = int(input("Player Two: Please select a number 1 to 9: "))
    userturn = userturn - 1
    #this sets the winning turn players number incase there is a win
    turn = 2
    #this checks if the user input is in the requred values
    if userturn > 8 or userturn < 0:
        #if not it give this message and prompts the player to make another selection
        print("Number is not 1 - 9")
        player_two()
    else:
        #else it checks if the spot is avalable is so it places their square down
        if game_board[userturn] == emty:
            game_board[userturn] = pl2
        else:
            #if not it prints this and prompts the player again
            print("Spot is Taken")
            player_two()
game_loop()

