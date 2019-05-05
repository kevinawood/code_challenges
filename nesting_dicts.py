# alien_0 = {'colour' : 'green', 'points' : 5}
# alien_1 = {'colour' : 'pink', 'points' : 10}
# alien_2 = {'colour' : 'blue', 'points' : 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(aliens)

aliens = []

for alien_number in range(30):
    new_alien = {'colour' : 'blue', 'points' : 15, 'speed': 'slow'}
    aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print('....')
#
# print('Total number of aliens: {}'.format(str(len(aliens))))

for alien in aliens[0:3]:
    if alien['colour'] == 'blue':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'blue':
            alien['colour'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
print(aliens)