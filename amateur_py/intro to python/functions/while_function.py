def formatted_name(firstname, lastname):
    full_name =  firstname + ' ' + lastname
    return full_name.title()

while True:
    print ("\n Please tell us your name: ")
    print ("Please enter 'q' anytime you want to quit from the program")
    f_name = input ("Enter your firstname please: ")
    s_name = input ("Enter your secondname please: ")

    #Code to quit from the program
    if f_name == 'q':
        break
    if s_name == 'q':
        break

get_formatted_name = formatted_name(f_name, s_name)
print ("\nHello! " + get_formatted_name)