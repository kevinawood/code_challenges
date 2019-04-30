# player_1 = {}
#
# player_1['name'] = input("What is your name?:\n")
# player_1['age'] = int(input("How old are you?:\n"))
#
# print(player_1)


alien_0 = {"colour": 'green', "points": 5, "x_position": "0", "y_position": "25", "speed": 'medium'}
print("Original x-position: {}".format(alien_0['x_position']))

# Move alien to the right
# Determine how far the alien moves based on its current speed
if alien_0["speed"] == 'slow':
    x_increment = 1
elif alien_0["speed"] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0["x_position"] = int(alien_0["x_position"] )+ int(x_increment)
print('New x-position is: {}'.format(alien_0["x_position"]))
#
# print(alien_0['colour'])
#
# new_points = alien_0['points']
# print("You just earned yourself {} points!".format(new_points))
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#
# print(alien_0)
#
# alien_0['colour'] = 'red'
#
# print(alien_0)





