# static method: Is really a method sits inside of a class but doesn't 
# have access to the CLS keyword or to the self keyword. It is just a function that belongs to that class.
## static attributes are same as class atributes in  python

class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)

s1 = Student("Tim", [80,45,76,87])
s2 = Student("vinay",[100,90,80,89])

average = Student.average_from_grades(s1.grades + s2.grades)

print(average)