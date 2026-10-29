#Class is a blueprint of an object
#Object is an instance of a class

class Employee:

   def __init__(self, name, gender, position):
       self.name = name
       self.gender = gender
       self.position = position



   def movement(self):
       print("Employee is walking")










employee1 = Employee("Mary", "Female", "CEO") #Creating an object
print(employee1.name)
print(employee1.gender)
print(employee1.position)
employee1.movement()


employee2 = Employee("John", "Male", "Admin")
print(employee2.name)
print(employee2.gender)
print(employee2.position)
employee2.movement()


