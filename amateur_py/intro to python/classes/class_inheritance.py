#When one class inherits from another class, it automatically takes the attributes and the methods of that class 
#The original class is called the parent class while the inheriting class is called a child class
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 30
        
    def get_drivers_id(self, drivers_id):
        return drivers_id    

    def get_descriptive_name(self):
        #Return a neatly formatted name
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def reset_odometer(self):
        self.odometer_reading = 0
        return self.odometer_reading

    def read_odometer(self):
        return "The car's current odometer reading is " + str(self.odometer_reading)
    
    #Modifying attribute value through a method
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer_reading = mileage
        else:
            print("You can't roll back mileage")

    def increment_mile(self, mile):
        self.odometer_reading += mile

class Battery():
    def __init__(self, battery_size = 80):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print ("This car has a " + str(self.battery_size) + " -kwh battery")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        #initialise attributes of the parent class
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tanks(): #Check this code later
        print("This car does not have gas tanks")

my_tesla = ElectricCar('Tesla', 'Tesla X', 2018)
my_tesla_data = my_tesla.get_descriptive_name()
print(my_tesla_data)
my_tesla.battery.describe_battery()