dream_vacation = {}

polling = True

while polling:
    name = input('What is your name?\n')
    dream = input("What is your dream destination?\n")

    dream_vacation[name] = dream

    repeat = input('Does another user want to respond? (yes/no)\n')
    if repeat.lower() == 'yes':
        continue
    else:
        polling = False
        break

for person, vacation in dream_vacation.items():
    print("{}'s dream vacation is {}".format(person, vacation))