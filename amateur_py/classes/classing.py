class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.welcome() #This method will automatically run when an instance of the class is called

    def welcome(self):
        print("Hey guys welcome to my dog class, lol!")

    def sit(self):
        print (self.name.title() + " is now sitted!")
    
    def rollover(self):
        print(self.name.title() + " has rolled over!")

    def get_age(self):
        print(self.name + " is " + str(self.age) + " years old!")

    def year(self, yob):
        year = 2018
        new_age = year - yob
        return new_age

    def get_new_name(self, new_name):
        self.name = new_name
        return self.name

SnoopyDog = Dog('Snoopy Dog', 6)
SnoopyDog.sit()
SnoopyDog.rollover()
SnoopyDog.get_age()
current_age = SnoopyDog.year(1995)
print("Snoopy has the age: " + str(current_age))
new_name = SnoopyDog.get_new_name("Yosabi")
print ("Snoopy's name is now changed to: " + new_name)