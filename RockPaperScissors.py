from random import randint

player = input("Please input rock (r), paper (p) or scissors (s): ")

print("You've selected {0}".format(player))

chosen = randint(1,3)
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

if player == computer:
    print("DRAW! You selected {0} and computer picked {1}".format(player, computer))

if player == 'r' and computer == 's':
    print("Congrats, you win you selected rock which beats scissors")
elif player == 'r' and computer == 'p':
    print("Sorry you lost, player picked {0} CPU picked {1}".format(player, computer))

if player == 'p' and computer == 'r':
    print("Congrats, you win you selected paper which beats rock")

elif player == 'p' and computer == 's':
    print("Sorry you lost, player picked {0} CPU picked {1}".format(player, computer))

if player == 's' and computer == 'p':
    print("Congrats, you win you selected scissors which beats papers")

elif player == 's' and computer == 'r':
    print("Sorry you lost, player picked {0} CPU picked {1}".format(player, computer))


