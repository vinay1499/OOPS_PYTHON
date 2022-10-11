#inheritance_3
# larger inheritance hierarchy

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


class Manager(Employee):
    def __init__(self,first_name, last_name, salary, department ):
        super().__init__(first_name,last_name,salary)     #overrided a constreuctor #I haven't passed self because super() method will implicitly pass self
        self.department = department

class Owner(Person):
    def __init__(self,first_name, last_name, net_worth ):
        super().__init__(first_name,last_name)     #overrided a constreuctor #I haven't passed self because super() method will implicitly pass self
        self.net_worth = net_worth







e = Employee("Sai Vinay", "Nandigam",120000)


print(isinstance(e,Owner))