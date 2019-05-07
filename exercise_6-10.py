favourite_numbers = {
    'kevin' : [4, 34, 12, 99],
    'shalom': [44, 23, 1],
    'amyke' : [2, 5, 00],
}

for number in favourite_numbers:
    print("{}'s favourite numbers are {}".format(number.title(), favourite_numbers[number]))