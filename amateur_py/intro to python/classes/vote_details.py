#Lists 
candidates = []
candidates.append("Dickson")
candidates.append("Scaver")
candidates.append("Flora")
candidates.append("Sanderson")

print(candidates)

for candidate in candidates:
    print ("\t- " + candidate)

#Dictionary
Voi_candidates = {
    'Mwangea' : 'Dickson',
    'Kaloleni' : 'Scaver',
    'Kariokor' : 'Flora',
    'Mazeras' : 'Sanderson' 
}

for region, Voi_candidate in Voi_candidates.items():
    print(region + " - " + Voi_candidate)

def animals(**entry):
    animal_lists = {}
    for key, value in entry.items():
        animal_lists[key] = value
    return animal_lists

my_animals = animals(reptile = 'lizard', carnivore = 'Lion', herbivorous = 'Cow')
print(my_animals)