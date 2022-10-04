#propeties

# don't name class names in plural.


class Person:
    def __init__(self,name):
        self.name = name
        self.salary = 0   # self._salary = 0; _salary is a private attribute (we can change the value in other languages but not in python.)

    # def set_salary(self,salary):
    #     if salary <0:
    #         raise ValueError("Hey, this is invalid!")
    #     self._salary = salary

    # def get_salary(self):
    #     return round(self._salary)

    # #salary = property(set_salary, get_salary)

    @property
    def salary(self):
        return round(self._salary)
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError("Hwy, this is invalid!")
        self._salary = salary 

p = Person("Tim")

p.salary = 100
print(p.salary)






