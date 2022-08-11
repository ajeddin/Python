

# list1 = ['','','']
# list2 = ['','','']
# list3 = ['','','']
# def display(list1, list2, list3):
#     print("Here is the current board: " )
#     print(list1)
#     print(list2)
#     print(list3)
    
# display(list1, list2, list3)
# def list_row_position():
#     playeronelist= []
#     playeronerow= []
#     playertwolist= []
#     playertworow= []
#     within_range= False
#     acceptable_range= range(0,3)
#         while playeronelist.isdigit() ==False:
#             playeronelist = input("Which line between 0 - 1 - 2 do you want to put X on? ")
#             if playeronelist.isdigit()== False:
#                 print("Please enter a number! ")
#             if playeronelist.isdigit() == True:
#                 if 




board = ['-','-','-','-','-','-','-','-','-','-']
def display(game_display):
    # clearoutput() might be useful 
    print(game_display[1]+'|' +game_display[2]+'|'+game_display[3])
    print(game_display[4]+'|' +game_display[5]+'|'+game_display[6])
    print(game_display[7]+'|' +game_display[8]+'|'+game_display[9])
display(board)
def user_input():
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
    return (playerone,playertwo)
playerone = user_input(playerone)
playertwo = user_input(playertwo)
user_input()
def user_choice():
    choice = ''
    acceptable_range= [1,2,3,4,5,6,7,8,9]
    within_range= False
    global turn
    turn = 0
    while choice.isdigit() == False or within_range==False:
        choice = input(f"Player 1, Where do you want to place your {playerone} (1-9): ")
        if choice.isdigit() == False:
            print("Please enter a digit betweeen 1-9: ")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range= True
                acceptable_range.remove(int(choice)) 
                board[int(choice)]= playerone
                turn +=1 
            else:
                print(f"Between {acceptable_range}")
                
    choice = ''
    within_range=False
    while choice.isdigit() == False or within_range==False:
        choice = input(f"Player 2, Where do you want to place your {playertwo} (1-9): ")
        if choice.isdigit() == False:
            print("Please enter a digit betweeen 1-9: ")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range= True
                acceptable_range.remove(int(choice)) 
                board[int(choice)]= playertwo
                turn +=1
            else:
                print(f"Between {acceptable_range}")
    return display(board)
user_choice()
playeronewin= False
playertwowin=False
draw = False
def no_win():
    playeronewin= False
    playertwowin=False
    draw = False
    while playeronewin ==False:
        if board[1] and board[2] and board[3] == playerone:
            playeronewin=True
        elif board[1] and board[4] and board[7] == playerone:
            playeronewin=True
        elif board[1] and board[5] and board[9] == playerone:
            playeronewin=True
        elif board[4] and board[5] and board[6] == playerone:
            playeronewin=True
        elif board[7] and board[8] and board[9] == playerone:
            playeronewin=True
        elif board[2] and board[5] and board[8] == playerone:
            playeronewin=True
        elif board[3] and board[6] and board[9] == playerone:
            playeronewin=True
        else:
            playeronewin= False
            break
    while playertwowin ==False:
        if board[1] and board[2] and board[3] == playertwo:
            playertwowin=True
        elif board[1] and board[4] and board[7] == playertwo:
            playertwowin=True
        elif board[1] and board[5] and board[9] == playertwo:
            playertwowin=True
        elif board[4] and board[5] and board[6] == playertwo:
            playertwowin=True
        elif board[7] and board[8] and board[9] == playertwo:
            playertwowin=True
        elif board[2] and board[5] and board[8] == playertwo:
            playertwowin=True
        elif board[3] and board[6] and board[9] == playertwo:
            playertwowin=True
        else:
            playertwowin=False    
            break
    if turn == 9:
        draw = True
    return playeronewin,playertwowin,draw
no_win()
scoreboard = [0,0]
def if_win():
    while playeronewin==True or playertwowin== True or draw==True:
        if playeronewin==True:
            scoreboard[0] +=1
            print('Player 1 has won!')
            break
        if playertwowin==True:
            scoreboard[1] +=1
            print('Player 2 has won!')
            break
        if draw == True:
            print("It's a draw")
            break
    while playeronewin==False and playertwowin== False and draw==False:
        user_choice()
        no_win()
if_win()
    
