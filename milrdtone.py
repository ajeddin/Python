

somevalue = "100"
print(somevalue.isdigit())
#  validating user input
def user_choice():
    choice = 'Wrong'
    acceptable_values= [1,2,3,4,5,6,7,8,9,10]
    while choice.isdigit() == False and choice in acceptable_values == False:
        
        choice = input("Please enter a number between (0-10): ")
        if choice.isdigit() == False:
            print("That's not a digit")
    return int(choice)
# TEST 
def func(s):
    s = s**2
    return num
print(func(3))
user_choice()