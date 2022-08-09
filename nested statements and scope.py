x  =25
def printer():
    x = 50
    return x
print(x)
# LEGB RULE Meaning Local - Enlosing funtion locals - Global - Built-in
#Lambda
lambda num:num**2

#  Global
name = 'This is a global string'
def greet():
    # Enclosing
    name = 'Sammy'
    def hello():
        # local
        name = 'I am local'
        print('Hello '+name)
    hello()
greet()


x= 50
def func(x):
    print(f'X is {x}')

    # local assignment
    x = 200
    print(f"i just changed {x} is x")
func(x)
x= 50
def func():
    global x
    print(f'X is {x}')

    # local assignment to global vairable
    x = 'NEW VALUE'
    print(f"i just changed {x} is x GLOBALY")
func()
print(x)