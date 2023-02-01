#METHODS


'''
A method is a function defined inside a class definition. There are three important kinds of methods they are:
instance methods, class methods, and static methods. 

'''



class Person:
    def __init__(self, name):  #this is a method, initialization method
        self.name = name
        self.age = None #if the user didn't give the age then it sets None value.
   

# age, weight,.. are attributes....

    def say_hello(self): # self acts as an instance of that class
        print(f"Hello, {self.name}")

    def set_age(self, age):  #this is called setter method, it sets tjhe age
        self.age = age

    def get_age(self):
        print(self.age)

p1 = Person("Tim")
p2 = Person("Susan")
p1.set_age(21)
p1.say_hello()
p2.say_hello()
print(p1.age)
p1.get_age()
p2.get_age()


# setters is a methed the takes in a value and assign it.

# getters get the value 




