#inheritance : allows one classs inherit or use functionality from another class.

# polymorphisms: The term polymorphism is originated from biology, where poly means many and morp-hism means forms. 
# In programming, polymorphism refers to the ability for an object to behave in different ways and exhibit different 
# behaviour based on the context it's used in. 


class Person:                           # super class or parent class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def say_hello(self):
        print(f"Hello, My name is {self.first_name} {self.last_name}")

class Employee(Person):  #inherited parent class
    def say_hello(self):                    #override, this override only works for the employee class.
        print("------------")
        super().say_hello()
        print("------------")


e = Employee("Sai Vinay", "Nandigam")
e.say_hello()

p = Person("joe","Blank")
p.say_hello()
      

