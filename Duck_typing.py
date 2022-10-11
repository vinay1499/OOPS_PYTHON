# Duck typing

class Duck:
    def swim(self):
        print("Swimming duck")
    
    def fly(self):
        print("Flying duck")

class Whale:
    def swim(self):
        print("Swimming whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
    animal.swim()
    animal.fly() #python tries and displays the error but other languages won't try.  


