# Person class
class Person:
    
    '''
    __init__ : Instantiate constructor.
    (self, name, age): Self is referring to the instance of our Person class. Name and age are parameters.
    self.name = name: Instance attribute
    self.age = age : Instance attribute
    '''
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age            
                                   

p1 = Person("Tim", 24)
p2 = Person("Bill", 32)

print(p1.name) 
print(p1.age)
print(p2.name)
print(p2.age)



class Fruit:
    
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        
a = Fruit("apple", 100)
print(a.name)
a.color = "red"
print(a.color)
