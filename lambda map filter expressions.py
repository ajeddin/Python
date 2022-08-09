def square(num):
    return num**2
my_num = [1,2,3,4,5]
map(square,my_num)
for item in map(square,my_num):
    print(item)
list(map(square,my_num))

def splicer(mystrong):
    if len(mystrong)%2 ==0:
        return "EVEN"
    else:
        return mystrong[0]

names = ['andy','eve','sally']
print(list(map(splicer,names)))
def check_even(num):
    return num %2 == 0
mynums=[1,2,3,45,6,7]
for n in filter(check_even,mynums):
    print(n)



def square(num):
    result = num**2
    return result
print(square(3))

def square(num): return num**2
print(square(3))

square = lambda num: num **2
print(square(2))
print(list(map(lambda num:num**2,my_num)))

print(list(filter(lambda num:num%2==0,mynums)))

print(list(map(lambda x:x[::-],names)))