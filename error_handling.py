# def add(n1,n2):
#     print(n1+n2)
# add(10,20)
# number1=10
# number2=input('Please provide number: ')
# add(number1,number2)
# print('Somthing Happened')
# print(result)


try:
    # Want to Attemt this code
    # may have a error
    result = 10 +"10"
except:
    print('Hey its looks like you arent adding correctly')
else:
    print('Add went well!')
    print(result)

try:
    f= open('testfile','r')
    f.write('Wrote a test line')
except TypeError:
    print('There was a type error')
except OSError:
    print('Hey you have an OS error')
finally:
    print("i always run")
def ask_for_int():
    try:
        result= int(input('Please provide number: '))
    except:
        print('woops!, this is not a number')
    finally:
        print('End of try/except/finally')
ask_for_int()
# while loop with exception handiling
def ask_for_int():
    while True:
        try:
            result= int(input('Please provide number: '))
        except:
            print('woops!, this is not a number')
            continue
        else:
            print('thanks')
            break
ask_for_int()