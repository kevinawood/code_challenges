# Deli Sandwiches

sandwich_orders = ['Deli', 'pastrami', 'Ham', 'Tuna', 'pastrami', 'Italiano', 'pastrami']
finished_orders = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print('I made you a {} sandwich\n'.format(sandwich))
    finished_orders.append(sandwich)

print('The sandwiches made were {}'.format(finished_orders))