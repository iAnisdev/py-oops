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
