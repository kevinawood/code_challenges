# player_1 = {}
#
# player_1['name'] = input("What is your name?:\n")
# player_1['age'] = int(input("How old are you?:\n"))
#
# print(player_1)

#
# alien_0 = {"colour": 'green', "points": 5, "x_position": "0", "y_position": "25", "speed": 'medium'}
# print(alien_0)
# print("Original x-position: {}".format(alien_0['x_position']))
#
# # Move alien to the right
# # Determine how far the alien moves based on its current speed
# if alien_0["speed"] == 'slow':
#     x_increment = 1
# elif alien_0["speed"] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# # The new position is the old position plus the increment
# alien_0["x_position"] = int(alien_0["x_position"] )+ int(x_increment)
# print('New x-position is: {}'.format(alien_0["x_position"]))
#
# # del alien_0["points"]
#
# print(alien_0)
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

# person = {'first_name': 'Jason', 'last_name': 'Anaro-Wood', 'age': 24, 'city': 'London'}
# print(person)

# favourite_numbers = {}
# count = 1
#
# while count < 5:
#     favourite_numbers['name'] = input('Whats your name?:\n')
#     favourite_numbers['number'] = int(input("What's your favourite number?: \n"))
#     count += 1
# print(favourite_numbers)

numbers = {"Jay": 5, "Kevin": 7, "Lucas": 99, "Rivaldo": 18, "sam": 23}

print(numbers["Jay"])
print(numbers["Kevin"])
print(numbers["Rivaldo"])

glossary = {'Dictionary': 'A Dictionary in Python is a...',
            "Variable": 'A Variable is used to store and reference information',

            }
print('Result found for !')
print("Result found for {}:".format(glossary['Dictionary']))