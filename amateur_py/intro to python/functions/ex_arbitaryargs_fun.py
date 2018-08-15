def order_sandwiches(*sandwich):
    sandwich_list = []
    sandwich_list.append(sandwich)
    return sandwich_list

order1 = order_sandwiches('Macaroni', 'Liver', 'Ugali', 'Eges')
print ("The following sandwishes have been ordered: ")
for sandwich in order1:
    print(sandwich)

def car_make(manufacturer, model, **other_info):
    car_now = {}
    car_now['manufacturer_name'] = manufacturer
    car_now['car_model'] = model
    for key, value in other_info.items():
        car_now[key] = value
    return car_now

car_1 = car_make('Subaru', 'SubFire', color = 'blue', horn = 'remble')
print(car_1)