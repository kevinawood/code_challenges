dalmatian = {
    'type' : 'Dog',
    'name' : 'Chow',
    'owner': 'Helena',

}

goldfish = {
    'type' : 'Goldfish',
    'name' : 'Nemo',
    'owner': 'Pete',
}

dragon = {
    'type' : 'Dragon',
    'name' : 'Kyogre',
    'owner': 'Lance'
}

pets = [dalmatian, goldfish, dragon]

for animal in pets:
    print('{}'.format(animal))