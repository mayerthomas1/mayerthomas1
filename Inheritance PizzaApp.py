class Pizza:

    def __init__(self, size, topping):


        self.size = size
        self.topping = topping


    def isVeggie(self):
        return False


    def isMeat(self):
        return False


class Meat(Pizza):


    def __init__(self, size, topping, cheese, crust):
        Pizza.__init__(size, topping)
        self.cheese = cheese
        self.crust = crust


    def isMeat(self):


        return True


    def isVeggie(self):


        return False


class Veggie(Pizza):


    def __init__(self, size, cheese, vegetables, crust):
        Pizza.__init__(self, size, cheese)

        self.vegetables = vegetables

        self.crust = crust


        def isVeggie(self):


            return True


def isPlain(self):
    return False

class Plain(Pizza):
    def __init__(self, size, crust):
        Pizza.__init__(size, crust)

        self.size = size

        self.crust = crust


def isPlain(self):
    return True


def isMeat(self):
    return False


Veggie1 = Pizza("Meatlovers", "Hamburger" ) 

print(Veggie1.size, Veggie1.isVeggie())

print("\n")

Veggie2 = Veggie("Cheesy Delight", 16, "Cheddar", "PepperJack")  

print(Veggie2.size, Veggie2.topping, Veggie2.crust, Veggie2.isVeggie(), Veggie2.isMeat())
