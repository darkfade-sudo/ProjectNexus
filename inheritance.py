
#Parent/Super/Base Class
class Animal:

    isMammal = True
    gender = "Male"
    age = 2

    def movement(self):
        print("Animal is moving")

#Child/Derived/Sub Class
class Cow(Animal):
    def moow(self):
        print("Cow is moowing")


 class Cat(Animal):
     def meow(self):
         print("Cat is meowing")

mycow = Cow()
mycow.moow()

mycat = Cat()
mycat.meow()
