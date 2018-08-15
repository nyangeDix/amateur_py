def make_pizza(size, *toppings):
    print ("Making an " + str(size) + " inch pizza with the following toppings")
    for topping in toppings:
        print("\t- " + topping)