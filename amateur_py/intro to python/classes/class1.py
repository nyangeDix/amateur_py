#Creating my first python class
#Class dog
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

class Restaurant():
    def __init__(self, restaurant_name, cuissine_type):
        self.restaurant_name = restaurant_name
        self.cuissine_type = cuissine_type
    
    def describe_restaurant(self):
        return self.restaurant_name + " has " + self.cuissine_type

    def open_restaurant(self):
        return self.restaurant_name + " is now open"

class User():
    def __init__(self, first_name, last_name, **user_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
    
    def describe_user(self):
        for key, values in self.user_profile.items():
            user_info = values
        return user_info

    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        return "How are you " + full_name + "!"

#User info 
user1 = User("Dickson", "Nyange", county = "Nairobi", country = "Kenya")
print (user1.describe_user())

my_dog = Dog('Snoopie', 10)
print ("My dog's name is " + my_dog.name.title())
print ("My dog's age is : " + str(my_dog.age))

#Accessing attributes
my_dog.name = 'Koki'
print ("I have changed my dog's name to : " + my_dog.name)

#Calling methods
my_dog.sit()
my_dog.roll_over()

Restaurant1 = Restaurant("Rose Wood", "Snacks") 
Restaurant2 = Restaurant("Liver Fool", "Wild Meat")
Restaurant3 = Restaurant("Tsavo Hotels", "Mushrooms")

print(Restaurant1.restaurant_name)
print(Restaurant1.cuissine_type)

print(Restaurant1.describe_restaurant())
print(Restaurant1.open_restaurant())


print(Restaurant2.restaurant_name)
print(Restaurant2.cuissine_type)

print(Restaurant2.describe_restaurant())
print(Restaurant2.open_restaurant())

print(Restaurant3.restaurant_name)
print(Restaurant3.cuissine_type)

print(Restaurant3.describe_restaurant())
print(Restaurant3.open_restaurant())
