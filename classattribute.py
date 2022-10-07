class Car:
    number_of_cars = 0

    def __init__(self,make,model):
        self.make = make
        self.model = model
        Car.number_of_cars +=1

c1 = Car('ford','fiesta')
print(Car.number_of_cars)
c2 = Car('toyata','corolla')
print(Car.number_of_cars)

