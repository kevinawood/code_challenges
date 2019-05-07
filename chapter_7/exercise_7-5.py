# Movie Tickets

age = 0
movie_ticket = 0
buying = True

while buying:
    age = int(input("What is your age: "))
    if 0 < age <= 3:
        print("Your ticket is free!\n")
        continue
    elif 12 >= age > 3:
        movie_ticket = 10
        print("Your ticket costs: ${}\n".format(movie_ticket))
        continue
    elif age == 0:
        print("Ending program...")
        buying = False
        break
    else:
        movie_ticket = 15
        print("Your ticket costs: ${}\n".format(movie_ticket))
