# arguments and keyword arguments
def myfunc(a,b,c=0,d=0,):
    # returns 5% of the sum of a and b
    return sum ((a,b,c,d)) *0.05
print(myfunc(40,60,40))

def myfunc(*args):
    return sum(args)*.5
print(myfunc(40,60,60,40,30,29))

def myfunc(**kwargs):
    print(kwargs)
    if "fruits" in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruits']))
    else:
        print('I did not find any fruits here ')
myfunc(fruits='apple', veggie='broccali')
def myfunc(*args, **kwargs):
    print(args and kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc(10,20,30, fruit = 'orange', food='eggs')