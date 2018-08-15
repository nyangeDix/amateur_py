#Defining a function
def make_tshirt(size = 'Large', t_message = 'I love python'):
    if size == 'Large':
        t_message
    elif size == 'Medium':
        t_message
    else:
        t_message = 'I love php'
    return t_message

def make_city(city = 'Nairobi', country = 'Kenya'):
    return city + " is in " + country
 
#make an argument optional
def full_name(firstname, lastname, secondname = ''):
    if secondname:
        name = firstname + ' ' + secondname + ' ' + lastname
    else:
        name = firstname + ' ' + lastname
    return name


#Returning a dictionary
def build_city(city_name, governor):
    #Build a list
    city_details = {'city':city_name, 'governor_name': governor}
    return city_details

#Call statements
t_shirt1 = make_tshirt(size = 'none')
print(t_shirt1)

city1 = make_city('Dodoma', 'Tanzania')
print(city1)

#Call optional argument function
full_name1 = full_name('Dickson','Nyange','Ngoji')
print(full_name1)
full_name2 = full_name('Dickson','Nyange')
print(full_name2
)

