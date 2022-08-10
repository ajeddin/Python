

somevalue = "100"
print(somevalue.isdigit())
#  validating user input
def user_choice():
    # INITIAL
    choice = 'Wrong'
    acceptable_values= range(0,11)
    within_range = False
    # 2 CONDITIONS TO CHECK
    # DIGIT or within range == False
    while choice.isdigit() == False or within_range == False:
        # DIGIT CHECK
        choice = input("Please enter a number between (0-10): ")
        if choice.isdigit() == False:
            print("That's not a digit")
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice)  in acceptable_values:
                within_range= True
            else:
                print("Out of range")
                within_range= False
            

    return int(choice)
user_choice() 

