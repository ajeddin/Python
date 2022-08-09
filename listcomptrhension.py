mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
# a more effeceint way
mylist = [letter for letter in mystring]
print(mylist)
# basically saying mylist = [element for element in "akakkaka" or mystring]
mynum = [num for num in range (0,12)]
print(mynum)
mynum = [num**2 for num in range (0,12)]
print(mynum)
mynum = [num for num in range (0,12) if num%2 ==0]
print(mynum)
print('\n')
celcius = [0,10,20,34.5]
fe = [((9/5)*temp + 32 ) for temp in celcius]
print(fe)
# take this easy at first and its not really easy to read
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

mylist2 = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist2.append(x*y)
print(mylist2)
# list comprehenstion version and be carful using tghem as they are not for beginners and hard to read
mylist2= [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist2)
