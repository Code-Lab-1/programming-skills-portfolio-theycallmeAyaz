#Exercise 1: Pizza Toppings
Pizza_Topping = "\nWhat Topping would you like?"
Pizza_Topping += "\nEnter 'quit' if you are done: "

while True:
    Topping = input(Pizza_Topping)
    if Topping != 'quit':
        print("\nI will add a  " + Topping + " topping to your pizza.")
    else:
        break
