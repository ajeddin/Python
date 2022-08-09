def say_hello():
    print("Hello")
print("\n")
say_hello()
#you need ()
def say_hello(name):
    print(f"Hello {name}")

say_hello("Jose")

def add_num(num1,num2):
    return num1+num2

def print_result(a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,20)
result =return_result(10,20)
print(result)