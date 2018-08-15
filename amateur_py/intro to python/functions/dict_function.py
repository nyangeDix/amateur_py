def buildPerson(name, gender, age = ''):
    #Input items into a dictionary
    person = {'personname' : name, 'persongender' : gender}

    if age:
        person['personage'] = age
    return person

buildPerson1 = buildPerson('Dickson', 'Male')
buildPerson2 = buildPerson('Sanderson', 'Male', str(22))

#get individual items for function
print ("Lets get the items in for person: ")
for details, values in buildPerson2.items():
    print ("\t- " + details + " : " + values)
