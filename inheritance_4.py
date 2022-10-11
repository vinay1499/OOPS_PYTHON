#inheritance
#multiple inheritance

class A:
    def __init__(self):
        print("A")



class B:
    def __init__(self):
        print("B")


class C(A,B):   #is A or B the parent classes. Both the classes are the parent classes, super classes for c. 
                #whatever we encounter first either A or B that gets executed
    pass

c = C()