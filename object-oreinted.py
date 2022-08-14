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
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots= spots
mydog = Dog(breed='Lab',name='Samy',spots=False)
print(mydog)
print(mydog.breed)
print(mydog.name)
print(mydog.spots)

