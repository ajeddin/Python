even = []
def lesser_even(a,b):
    if (a %2 !=0) or (b %2 !=0):
        result = max(a,b)
    elif (a %2 ==0) and (b %2==0):
        result = min(a,b)
    return result
print(lesser_even(4,9))

def animal_cracker(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]
print(animal_cracker('Hello horld'))

def tw_enty(a,b):
    if a == 20 or b == 20 or (a+b==20):
        return True
    else:
        return False
print(tw_enty(20,21))
print(tw_enty(19,1))
print(tw_enty(15,4))

def m_ac(text):
    first = text[0]
    fourthletter= text[3]
    inbetween= text[1:3]
    rest = text[4:]

    return first.upper() + inbetween + fourthletter.upper() + rest
print(m_ac("macdonald"))
def m_ac(text):
    first = text[:3]
    second=text[3:]
    return first.capitalize()+second.capitalize()
print(m_ac("macdonald"))

def rever_sed(text):
    word = text.split()
    wordreveresed = word[::-1]
    return (' ').join(wordreveresed)

print(rever_sed('i am home'))
def almost_there(n):
    return (abs(100-n) <=10) or (abs(200 - n) <=10)
print(almost_there(11))

def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result
print(paper_doll("hello"))
def summer_59(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num !=5:
                total += num
                break
            else:
                add = False
        while not add:
            if num !=9:
                break
            else:
                add = True
                break
    return total
print(summer_59([1,3,4,5,6,5,2,5,9,7,9]))
def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    print(code)
    return len(code) ==1

print(spy_game([1,0,2,3,0,7,0]))

