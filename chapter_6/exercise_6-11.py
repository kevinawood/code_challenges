cities = {
    'London' : {
        'country' : 'England',
        'continent' : 'Europe',
        'population': 8000000,
    },
    'Paris' : {
        'country' : 'France',
        'continent' : 'Europe',
        'population' : 5000000,
    },
    'Perth' : {
        'country' : 'Australia',
        'continent' : 'Australia',
        'population': 3000000
    }
}

for city, city_info in cities.items():
    print('{} \n {}'.format(city, city_info))