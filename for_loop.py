loop = [1,2,3,4,5,67,8,9]
for loopy in loop:
    if loopy % 2 ==0:
      print(loopy)
    else:
        print(f"Odd Number: {loopy}")
list_sum = 0

for loopy in loop:
    list_sum= list_sum+loopy

print(list_sum)
string_ex= 'Hello mY boy'
for letter in string_ex:
    if letter == letter.upper():
        print(letter)

tupex = [(1,2), (3,4),(5,6)]
for item in tupex:
    print(item)

for a, b in tupex:
    print(b)

mylist = [(1,2,3),(4,5,6), (7,8,9)]
for a,b,c in mylist:
    print(c)
d = {'k1':1,'k2':4,'k3':2 }
for item,value in d.items():
    print(value)