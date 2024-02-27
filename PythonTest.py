class Vehicle:


    def __init__(self, make, model):


        self.make = make

        self.model = model


    def isBus(self):


        return False


    def isCar(self):


        return False


class Car(Vehicle):


    def __init__(self, make, model, mileage, wheels):


        Vehicle.__init__(make, model)

        self.mileage = mileage

        self.wheels = wheels


        def isCar(self):


            return True


def isBus(self):


    return False


class Bus(Vehicle):


    def __init__(self, make, model, capacity, wheels):


        Vehicle.__init__(self, make, model)

        self.capacity = capacity

        self.wheels = wheels


        def isBus(self):


            return True


def isTruck(self):


        return False


class Truck(Vehicle):


    def __init__(self, make, model, size, wheels):


        Vehicle.__init__(make, model)

        self.size = size

        self.wheels = wheels


        def isTruck(self):


            return True


def isCar(self):


    return False


bus1 = Vehicle("jaguar", 1995)  # An Object of vechile

print(bus1.make, bus1.isBus())

print("\n")

bus2 = Bus("TATA", 2005, 100, 4)  # An Object of Bus

print(bus2.make, bus2.model, bus2.wheels, bus2.isBus(), bus2.isCar())
