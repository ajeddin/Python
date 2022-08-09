# dict vs list basically in dict
# you cant get them by key name but with lists you have to retreive it by location.

mydict = {'milk': '$3.29', 'apple':'$1.29','onion':'$4'}
print(mydict['milk'])
dict= {'k1': ['d','c','s']}
print(dict['k1'])
letter = dict["k1"][2]
print(letter.upper())
dict['k3']=500
print(dict)
#dict['k3'] = input("What is your name? ")
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())

