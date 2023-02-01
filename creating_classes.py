'''

'''
# initializing an object using __init__ method. 

# class Person:
#     pass

# p1 = Person()
# print(type(p1))

# class Person:
#     def __init__(self):         # __init__ is called dondeer method
#         print("ran")

# p1 = Person()
# print(type(p1))

# class Person:
#     def __init__(self, x):         # __init__ is called dondeer method
#         print(x)

# p1 = Person(2)
# print(type(p1))


# class Person:
#     def __init__(self, name):         # __init__ is called dondeer method
#         self.name = name            # created an attribute.
#                                     # you can assume self being p1, p2.....;

# p1 = Person("Tim")
# p2 = Person("Bill")

# print(p1.name) # p1.name == self.name
# print(p2.name)


class Person:
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
