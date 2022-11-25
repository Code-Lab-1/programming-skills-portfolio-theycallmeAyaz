expensive_car = int(input("Enter the price = "))
if expensive_car <= 11500:
    print("the car is below affordable budget.")
elif expensive_car <= 19999:
    print("the car is at affordable budget.")
elif expensive_car <= 30000:
    print("the car is above affordable budget.")
else: print("The car is expensive.")