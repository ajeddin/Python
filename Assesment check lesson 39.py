st = 'Print only the words that Start with s in this sentence'
for word in st.split():
    if word[0] == "s" or word[0]=="S": # or if word[0].lower == "s":
        print(word)



mynum = [num for num in range(0,11)]
for x in mynum:
    if x %2==0:
        print(x)



hello=  [n for n in range(1,51) if n%3==0]
print(hello)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) %2 == 0:
        print(word+ " is even")
# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are
# multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num %3 == 0 and num %5==0:
        print("FizzBuzz")
    elif num %5==0:
        print("Buzz")
    elif num %3==0:
        print("Fizz")
    else:
        print(num)
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])
