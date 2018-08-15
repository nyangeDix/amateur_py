class Fruits():
    def __init__(self, fruit):
        self.fruit = fruit
        self.fruits = []
    
    def get_fruits(self, fruit):
        my_list = self.fruits
        my_list.append(self.fruit)
        return my_list

my_fruit = Fruits('fruits')
my_fruit_list = my_fruit.fruits
#flag
fruit_flag = True
while fruit_flag:
    fruit_name = input("Enter fruit name: ")
    fruit_list = my_fruit.get_fruits(fruit_name)
    if fruit_name == 'q':
        break

print(my_fruit_list)