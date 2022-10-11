#inheritance 2

#override a constructor 

class Person:                           # super class or parent class
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def say_hello(self):
        print(f"Hello, My name is {self.first_name} {self.last_name}")


class Employee(Person):  #inherited parent class
    def __init__(self,first_name, last_name, salary ):
        super().__init__(first_name,last_name)     #overrided a constreuctor #I haven't passed self because super() method will implicitly pass self
        self.salary = salary


    def say_hello(self):                    #override, this override only works for the employee class.
        super().say_hello()
        print(f"My salary is {self.salary}")


e = Employee("Sai Vinay", "Nandigam",120000)
e.say_hello()
        
