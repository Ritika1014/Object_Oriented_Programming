class Animal:
    def sound(self):
        print("Animals make different sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animals=[Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()
