from cgi import print_directory
from re import X


def vol(rad):
    volume = (((rad **3) * 3.14) *  (4/3))
    limited_float = round(volume, 2)

    return limited_float
print(vol(2))

def ran_check(num,low,high):
    if low < num < high:
        return (f"{num} is in the range between {low} and {high}")

print(ran_check(5,2,7))
def ran_check(num,low,high):
    return num in range(low, high+1)


print(ran_check(5,2,7))
s= 'Hello Mr.Rogers, how are you this fine Tuesday?'
def up_low(s):
    up = 0
    low = 0 
    # letter = [x for x in s]
    for x in s :
        if x.isupper() == True:
            up +=1 
        elif x.islower() == True:
            low +=1
        else:
            continue
    return f"Original String: {s}\nNo. of Upper case characters: {up}\nNo. of Lower case characters: {low}"
print(up_low(s))

lister = [1,1,1,1,2,2,2,2,2,3,3,4,4,5,5]
def unique(s):
    listnew = []
    for x in s:
        if x in listnew:
            pass
        else:
            listnew.append(x)
    return listnew
print(unique(lister))
def unique(s):
    return list(set(lister))
print(unique(lister))
lst = [1,2,3,-4]

def multi(num):
    result = 1
    for x in num:
        result = result *x
    return result
print(multi(lst))
def palindrome(s):
    sspace= s.replace(" ", "")
    return sspace[::-1] == s

print(palindrome("race car"))
import string
my = "the Quick brown fox jums over the lazy dog"

def pang(s):
    hello = string.ascii_lowercase
    helloo = set(hello)
    s = s.replace(" ","")
    s = s.lower()
    ss= set(s)
    return ss == helloo 
print(pang(my))

