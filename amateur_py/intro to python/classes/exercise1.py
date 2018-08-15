class Restaurant():
    def __init__(self, restaurant_name, cuissine_type):
        self.restaurant_name = restaurant_name
        self.cuissine_type = cuissine_type 
        self.number_served = 0 
    
    def describe_restaurant(self):
        return self.restaurant_name + " has " + self.cuissine_type

    def open_restaurant(self):
        return self.restaurant_name + " is now open"

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

restaurant1 = Restaurant('Safari Restaurant', 'WildBeast Meat')
#restaurant1.number_served = 25
restaurant1.set_number_served(100)
restaurant1.increment_number_served(200)
customers_served = restaurant1.number_served
print("Current no. of customers served: " + str(customers_served))

print ("\n The below code is for another piece of excerise...")

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        return "How are you " + full_name + "!"
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
new_user = User('Dickson', 'Nyange')
new_user.increment_login_attempts() #Call the increment
new_user.reset_login_attempts()
new_attempts = new_user.login_attempts #Call the current number
print("Current attempts: " + str(new_attempts))

print("\nSecond class instance.....")
new_user2 = User('Sanderson', 'Mwakamba')
new_user2.increment_login_attempts()
new_user2.increment_login_attempts()
new_user2.increment_login_attempts()
new_user2.increment_login_attempts()
current_attempts = new_user2.login_attempts
print("Second User Login Attempts: " + str(current_attempts))
new_user2.reset_login_attempts()
current_attempts = new_user2.login_attempts
print("The attempts for the second user have been reset to: " + str(current_attempts))