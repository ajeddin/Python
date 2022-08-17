# base class
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print("I am eating")
# Derived Class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def who_am_i(self):
        print('I am a Dog')
    def bark(self):
        print('WOOF!!')
    def eat(self):
        print('I am a dog and i am eating')
mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()
