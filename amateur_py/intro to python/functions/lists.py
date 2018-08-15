#Passing a list to a function
def greet(names):
    for name in names:
        print ("Hello! " + name)

def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print("Printing model: " + current_model)
        completed_models.append(current_model)

def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_models = ['Techno phone case', 'Toshiba laptop case', 'Robot head']
completed_models = []
print_models(unprinted_models[:], completed_models)
print("List below shows completed models:.... ")
show_completed_models(completed_models)

#Arbitary values - more than one value in a function
#Python handles arbitary values as lists
def pizza(size, *toppings):
    print ("Mustapha wants pizza of size " + str(size) + " with the following toppings: ")
    for topping in toppings:
        print("\t-" + topping)

pizza(21, 'ugalie', 'samosa', 'pojo')

#Arbituary arguments that accepts as many data as possible
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)

def my_life(name, career, **other_details):
    personal_details = {}
    personal_details['my_name'] = name
    personal_details['my_career'] = career
    for key, value in other_details.items():
        personal_details[key] = value
    return personal_details

my_life1 = my_life('Dickson', 'Software Engineer', gender = 'male', career_specialisation = 'Data Scientist')
print(my_life1)