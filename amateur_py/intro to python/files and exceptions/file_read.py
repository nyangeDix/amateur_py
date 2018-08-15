#check for the current programs directory
from os import path

print(path.abspath())

#Open the file 
f = open('ligma.txt', 'r')

print(f.name)

#Close the file after down with it
f.close()