#properties2

class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self,second):
        if second<0 or second>60:
            raise ValueError("Hey, this is invalid")
            self._second = second

t = Time(54)
t.second = 59
print(t.second)


#or


# class Time:
#     def __init__(self, second):
#         self._second = second


#     def get_second(self):
#         return self._second


#     def set_second(self,second):
#         if second<0 or second>60:
#             raise ValueError("Hey, this is invalid")
#             self._second = second
#     second = property(get_second,set_second)
# t = Time(54)
# t.second = 59
# print(t.second)
