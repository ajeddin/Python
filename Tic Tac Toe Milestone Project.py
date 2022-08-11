

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
    return playerone and playertwo
user_input()
def user_choice():
    choice = ''
    acceptable_range= [1,2,3,4,5,6,7,8,9]
    within_range= False
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
                print(acceptable_range)
            else:
                print("Between 1-9")
                
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
                print(turn)
            else:
                print("Between 1-9")
    return display(board)
user_choice()
# def no_win():
    