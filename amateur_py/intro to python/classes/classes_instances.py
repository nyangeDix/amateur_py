class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 30

    def get_descriptive_name(self):
        #Return a neatly formatted name
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def odometer_reading(self):
        return "The car's current odometer reading is " + str(self.odometer)
    
    #Modifying attribute value through a method
    def update_reading(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back mileage")

    def increment_mile(self, mile):
        self.odometer += mile

my_new_car = Car('Hyundai', 'Hyundai4', 2018)

#Modifiying attribute values from the class
my_new_car.update_reading(40)
my_new_car.increment_mile(50)
my_odometer_reading = my_new_car.odometer_reading() 
print(my_new_car.get_descriptive_name())
print(my_odometer_reading)