# Multiples of Ten

user_number = int(input("Please enter a number: "))

if user_number % 10 == 0:
    print("{} is a multiple of 10".format(user_number))
else:
    print("{} is not a multiple of 10".format(user_number))