class Vehicle:
    def __init__(self, make, model, year, type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
    
honda = Vehicle('Honda', 'Civic', 2019, 'car')
print(honda.make , honda.model, honda.year, honda.type)

bike = Vehicle('Honda', 'CBR', 2019, 'motorcycle')
print(bike.make , bike.model, bike.year, bike.type)

class Car(Vehicle):
    def __init__(self, make, model, year, type, doors):
        super().__init__(make, model, year, type)
        self.doors = doors

civic = Car('Honda', 'Civic', 2019, 'car', 4)

print(civic.make , civic.model, civic.year, civic.type, civic.doors)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type, engine):
        super().__init__(make, model, year, type)
        self.engine = engine

cbr = Motorcycle('Honda', 'CBR', 2019, 'motorcycle', '1000cc')

print(cbr.make , cbr.model, cbr.year, cbr.type, cbr.engine)