# Pizza Toppings

while True:
    topping = input("What pizza topping would you like to add? (Type 'quit' to stop): \n")

    if topping.lower() in ['quit', 'q'] :
        print("Ending program...")
        break
    else:
        print("{} added. \n".format(topping))
        continue
