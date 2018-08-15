#Learn how to import and to use modules
#Importing the whole modules
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(20, 'mushroom')

#Importing special functions
from pizza import make_pizza
make_pizza(21, 'Eggs', 'Cheese', 'Masala')
make_pizza(21, 'Mushrooms', 'Special mint leaves')

#Use a give a function alies name
from pizza import make_pizza as limbo
limbo(48, 'Macoroni', 'Masala')

#Using as to give a module alias name
import pizza as k
k.make_pizza(10, 'Mushroom')

#Importing all functions in a modules
from pizza import *
pizza.make_pizza(15, 'Fungus')