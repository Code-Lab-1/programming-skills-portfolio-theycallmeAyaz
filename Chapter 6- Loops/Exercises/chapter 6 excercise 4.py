sandwich_orders = ["\nVegetarian","\nBeef","\nChicken tikka","\nBoiled Egg"]
prepared_sandwiches = []
while sandwich_orders:
    almost_done_sandwich = sandwich_orders.pop()
    print("\n"+ almost_done_sandwich + " sandwich"+" is almost prepared.")
    prepared_sandwiches.append(almost_done_sandwich)
print("\n")
for sandwich in prepared_sandwiches:
    print("\nSandwich prepared: " + sandwich + " sandwich.")