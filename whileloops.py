x= 0
y = [1,2,3]
while x < 5:
    print(f"the current value is x is {x}")
    x = x+1
else:
    print("X is more than 5")
for item in y:
    pass #bassicaly passes doesnt do anything
for item in y:
    if item == 2:
        continue #goes back
    print(item)

for item in y:
    if item == 2:
        break #breaks out b
    print(item)
