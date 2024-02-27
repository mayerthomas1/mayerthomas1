class BusinessHeirarchy:
#represent different employees in a business
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
        

class CEO (BusinessHeirarchy):

    def __init__(self, name, age, salary):
        BusinessHeirarchy.__init__(self, name, age)
        self.salary = salary
    def info(self):
        BusinessHeirarchy.info(self)
        print('Salary: "{:d}"'.format(self.salary))


class CFO(BusinessHeirarchy):

    def __init__(self, name, age, totalrevenue):
        BusinessHeirarchy.__init__(self, name, age)
        self.totalrevenue = totalrevenue
    def info(self):
        BusinessHeirarchy.info(self)
        print('TotalRevenue: "{:d}"'.format(self.totalrevenue))

#some other examples of classes that would fit in here
class HR(BusinessHeirarchy):
    
    def __init__(self, name, age, number_of_employees):
        BusinessHeirarchy.__init__(self, name, age)
        self.number_of_employees = number_of_employees
    def info(self):
        BusinessHeirarchy.info(self)
        print('Number of Employees: "{:d}"'.format(self.number_of_employees))

#class IT(BusinessHeirarchy):
    #def __init__(self, name, age, PC_parts_needed):
    #BusinessHeirarchy.__init__(self, name, age)
    #self.PC_parts_needed = PC_parts_needed
        


c= CEO('Phillip Calvin McGraw', 72, 100000)
f= CFO('Judith Sheindlin', 80, 1000000000)
h= HR('Terry Bollette',68, 1000)

print()

associates = [c, f, h]
for associate in associates:
    associate.info()