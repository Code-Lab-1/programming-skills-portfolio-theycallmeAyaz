# Exercise 5: No Pastrami
Sandwich_menu = ["\nVegetarian","\nBeef","pastrami","\nChicken tikka","pastrami","\nBoiled Egg","pastrami"]
prepared_sandwiches = []
print("I apologize we ran out of pastrami today.")
while 'pastrami' in Sandwich_menu:
    Sandwich_menu.remove('pastrami')

print("\n")
while Sandwich_menu:
    almost_done_sandwich = Sandwich_menu.pop()
    print("\n"+ almost_done_sandwich + " sandwich"+" is almost prepared.")
    prepared_sandwiches.append(almost_done_sandwich)
print("\n")
for sandwich in prepared_sandwiches:
    print("\nSandwich prepared: " + sandwich + " sandwich.")

    