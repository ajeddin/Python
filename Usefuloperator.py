for num in range(0,10,2):
    print(num)
print(list(range(0,11,2)))
index_count= 0
for letter in "abcde":
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
mylist3 = [100,200,300,400,500,600]
for item in zip(mylist1,mylist2,mylist3):
    print(item)
print(list(zip(mylist1,mylist2,mylist3)))
'x' in [1,2,3]
print("x" in (1,2,3))
mylist4 = [1,2,3,4,5,6,34,64,23,76]

print(min(mylist4))
print(max(mylist4))
from random import shuffle
mylist5 = [1,2,3,45,6,7,8,9]
print(mylist5)
shuffle(mylist5)
print(mylist5)

from random import randint
print(randint(0,100))

