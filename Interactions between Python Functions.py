from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
mylistgame = ["","O", ""]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(mylistgame)
print(result)
def player_guess():
    guess=''
    while guess not in ["0","1","2"]:
         guess = input("Pick a number: 0,1,2 ")
    return int(guess)
guess=  player_guess()
# myindex = player_guess()
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct! ")
    else:
        print("Wrong guess!")
        print(mylist)
check_guess(result,guess)
