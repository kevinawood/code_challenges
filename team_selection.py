from random import  choice

players = []
teamname = []
file = open('players.txt', 'r')
players = file.read().splitlines()

file = open('team.txt', 'r')
teamnameA = choice(file.read().splitlines())

file = open('team.txt', 'r')
teamnameB = choice(file.read().splitlines())
print(players)

teamA = []
teamB = []

while len(players) > 0:
    player1 = choice(players)
    teamA.append(player1)
    players.remove(player1)

    if players == []:
        break

    player2 = choice(players)
    teamB.append(player2)
    players.remove(player2)

print("Team {0}: ".format(teamnameA))
print("Team members {0}".format(teamA))
print("Team {0}: ".format(teamnameB))
print("Team members {0}".format(teamB))

