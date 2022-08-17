# base class Inheritance 
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
# Polymorphism
class Dog():
    def __init__(self,name):
        self.name= name
    def speak(self):
        return self.name + ' says woof'
class Cat():
    def __init__(self,name):
        self.name= name
    def speak(self):
        return self.name + ' says meow!'
neko= Dog('neko')
felix= Cat('Felix')
print(felix.speak())
for pets in [neko,felix]:
    print(type(pets))
    print(pets.speak())
class Animal():
    def __init__(self,name):
        self.name=name
    def speak (self):
        raise NotImplementedError("Subclass must implement this abstract method")
class Dog():
    def speak(self):
        return self.name+ ' says woof!'
class Cat():
    def speak(self):
        return self.name+ ' says meow!!'
fido=Dog(fido)
isis = Cat(isis)
