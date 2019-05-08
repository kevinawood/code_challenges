# Deli Sandwiches

sandwich_orders = ['Deli', 'Ham', 'Tuna', 'Italiano']
finished_orders = []

for sandwich in sandwich_orders:
    print('I made you a {} sandwich\n'.format(sandwich))
    finished_orders.append(sandwich)

print('The sandwiches made were {}'.format(finished_orders))