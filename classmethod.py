class Circle:
    pi = 3.14

    @classmethod
    def area(cls,radius):
        return cls.pi * (radius**2)
    
    @classmethod
    def perimeter(cls,radius):
        return 2 * cls.pi * radius
    
    @classmethod
    def get_preimeter_and_radius(cls,radius):
        return (cls.perimeter(radius), cls.area(radius))

print(Circle.get_preimeter_and_radius(5))