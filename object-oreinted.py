mylist= [1,2,3]
myset= set()
print(type(myset))

class Sample():
    pass
mysample = Sample()
print(mysample)
class Dog():
    def __init__(self,breed):
        self.breed = breed
mydog = Dog(breed='Lab')
print(mydog)
print(mydog.breed)
class Dog():
    # class object attribute same for any instance of a class 
    species = 'Mammal'

    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots= spots
    # operations/Actions ---> Methods
    def bark(self):
        print("WOOF!")
mydog = Dog(breed='Lab',name='Samy',spots=False)
print(mydog)
print(mydog.breed)
print(mydog.name)
print(mydog.spots)
print(mydog.species)
class Dog():
    # class object attribute same for any instance of a class 
    species = 'Mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    # operations/Actions ---> Methods
    def bark(self,number):
        print(f"WOOF!, My name is {self.name} and the number is {number}")
mydog = Dog('Lab','Samy')
print(mydog.breed)
print(mydog.name)
mydog.bark(10)
class Circle():
    #  Class Object Attribute
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area= radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius* self.pi*2
mycircle = Circle(30)
print(mycircle.radius)
print(mycircle.get_circumference())
print(mycircle.area)