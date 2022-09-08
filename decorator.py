def func():
    return 1
func()
def hello():
    print('Hello!')
greet = hello
greet()
del hello
greet()
def hello(name='Jose'):
    print('The hello() function has been executed')
    def greet():
        return '\t This is the greet() func inside hello'
    def welcome():
        return '\t This is inside the welcome function'
    print('i am going to return a function!')
    if name == 'Jose':
        return greet
    else:
        return welcome
hello()
greet()
mynewfunc = hello('Jose')
print(mynewfunc())
mynewfunc = hello('Jos')
print(mynewfunc())
def cool():
    def super_cool():
        return 'i am very cool!'
    return super_cool
somefunc= cool()
print(somefunc())

def hello():
    return 'Hi Jose'
def other(somefunc):
    print('other code runs here!')
    print(somefunc())
other(hello)

def new_decorator(orgiinalfunc):
    def wrap_func():
        print('Some exra code, before the origninal function')
        orgiinalfunc()
        print('some extra code after original code')
    return(wrap_func)
def func_need_decoratpr():
    print('i want to be decorator')
decorated_func=new_decorator(func_need_decoratpr)
decorated_func()

@new_decorator
def needdec():
    print('i want to be decorated')
needdec()