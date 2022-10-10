# class and static method

class Student:
    grade_bump = 2.0   #static attribute ot class attribute.
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    #instance method

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_from_grades_plus_bump(cls,grades):
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)



    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)

s1 = Student("Tim", [80,45,76,87])
s2 = Student("vinay",[100,90,80,89])

average = Student.average_from_grades(s1.grades )

average2 = Student.average_from_grades_plus_bump(s1.grades )

print(average2)