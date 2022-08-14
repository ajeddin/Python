board = ['-','-','-','-','-','-','-','-','-']
def display(game_display):
    # clearoutput() might be useful 
    print(game_display[0]+'|' +game_display[1]+'|'+game_display[2])
    print(game_display[3]+'|' +game_display[4]+'|'+game_display[5])
    print(game_display[6]+'|' +game_display[7]+'|'+game_display[8])
display(board)
def user_input():
    global playerone
    global playertwo
    playerone = ''
    playertwo = ''
    Acceptable_values= ['X','O']
    while playerone not in Acceptable_values:
        playerone = input('PLayer 1, Please choose your character (X or O): ')
        if playerone not in Acceptable_values:
            print("Character between X and O")
        if playerone in Acceptable_values:
            # Acceptable_values.remove(playerone)
            # playertwo= Acceptable_values
            if playerone == "X":
                playertwo = "O"
            else:
                playertwo= "X"
            print(f"Player 2 your marker is {playertwo}")
            break
user_input()
def user_choice():
    choice = ''
    acceptable_range= [0,1,2,3,4,5,6,7,8]
    within_range= False
    global turn
    turn = 0

    while choice.isdigit() == False or within_range==False:
        choice = input(f"Player 1, Where do you want to place your {playerone} (1-9): ")

        if choice.isdigit() == False:
            print("Please enter a digit betweeen 1-9: ")
        if choice.isdigit() == True:
            choice= int(choice)-1

            if choice in acceptable_range:
                within_range= True
                acceptable_range.remove(choice) 
                board[choice]= playerone
                turn +=1 
                display(board)

                break
            else:
                print(f"Between {acceptable_range}")
                choice= str(choice)
        

                
    choice = ''
    within_range=False
    while choice.isdigit() == False or within_range==False:
        choice = input(f"Player 2, Where do you want to place your {playertwo} (1-9): ")
        if choice.isdigit() == False:
            print("Please enter a digit betweeen 1-9: ")
        if choice.isdigit() == True:
            choice= int(choice)-1
            if choice in acceptable_range:
                within_range= True
                acceptable_range.remove(choice) 
                board[choice]= playertwo
                turn +=1 
                break
            else:
                print(f"Between {acceptable_range}")
                choice= str(choice)

    return display(board)
user_choice()
def no_win():
    global playeronewin
    global playertwowin
    global draw
    playeronewin= False
    playertwowin=False
    draw = False
    while playeronewin ==False:
        if board[0]  == playerone and board[1] == playerone and board[2] == playerone:
            playeronewin=True
        elif board[0] == playerone and board[3] == playerone and board[6] == playerone:
            playeronewin=True
        elif board[0] == playerone and board[4] == playerone and board[8] == playerone:
            playeronewin=True
        elif board[3] == playerone and board[4] == playerone and board[5] == playerone:
            playeronewin=True
        elif board[6] == playerone and board[7] == playerone and board[8] == playerone:
            playeronewin=True
        elif board[1] == playerone and board[4] == playerone and board[7] == playerone:
            playeronewin=True
        elif board[2] == playerone and board[5] == playerone and board[8] == playerone:
            playeronewin=True
        else:
            playeronewin= False
            break
    while playertwowin ==False:
        if board[0] == playerone and board[1] == playerone and board[2] == playertwo:
            playertwowin=True
        elif board[0] == playerone and board[3] == playerone and board[6] == playertwo:
            playertwowin=True
        elif board[0] == playerone and board[4] == playerone and board[8] == playertwo:
            playertwowin=True
        elif board[3] == playerone and board[4] == playerone and board[5] == playertwo:
            playertwowin=True
        elif board[6] == playerone and board[7] == playerone and board[8] == playertwo:
            playertwowin=True
        elif board[1] == playerone and board[4] == playerone and board[7] == playertwo:
            playertwowin=True
        elif board[2] == playerone and board[5] == playerone and board[8] == playertwo:
            playertwowin=True
        else:
            playertwowin=False    
            break
    if turn == 8:
        draw = True
no_win()
def if_win():
    while playeronewin==False or playertwowin== False or draw==False:
        if playeronewin==True:
            print('Player 1 has won!')
            break
        if playertwowin==True:
            print('Player 2 has won!')
            break
        if draw == True:
            print("It's a draw")
            break
        else:
            user_choice()
            no_win()
if_win()

def gameon_choice():
    choices = 'WRONG'

    while choices not in ['Y', 'N']:
        choices= input("Do you want to continue playing (Y or N): ")
        if choices not in ['Y', 'N']:
            print("Sorry, I don't understand, Please choose Y or N: ")
    if choices== "Y":
        return True
    else:
        return False
game_on= gameon_choice()
board = ['-','-','-','-','-','-','-','-','-','-']
while game_on:
    display(board)
    user_input()
    user_choice()
    no_win()
    if_win()
    game_on=gameon_choice()
    
