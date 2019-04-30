import random
import time

coin = ['Heads', 'Tails']
outcomes = []


def flip(amount):
    for i in range(0, amount):
        outcomes.append(random.choice(coin))
    results()

def results():
    heads = 0
    tails = 0
    print("The results are as follows:\n")
    for result in outcomes:
        if result == "Heads":
            heads += 1
        else:
            tails += 1
    print("Heads: {}, Tails: {}".format(heads, tails))
    print(outcomes)


def main():
    print("Coin flip simulator...")
    time.sleep(1)
    amount = int(input("How many times do you want to flip the coin?: \n"))
    flip(amount)

print(outcomes)

if __name__ == "__main__":
    main()


