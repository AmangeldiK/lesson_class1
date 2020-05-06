class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = False
    
    def __str__(self):
        return f'{self.make} {self.model}, {self.year}, {self.max_speed}, {self.odometer}, {self.is_flying}'
    
    def take_off(self):
        self.is_flying = True
        #return True


    def fly(self):
        self.odometer = 2300
        return self.odometer
        
    



    def land(self):
        self.is_flying = False

air = Airplane('Herpa', 'Boeing-777', '2008-release', 'max_speed-905km/h', 3000)
air.take_off()
air.fly()
air.land()
print(air)


