Ticket_Sales_Person = 'Enter your Age:\n'
Ticket_Sales_Person += "\nEnter 'quit' Once you are done"

while True:
    Age = input(Ticket_Sales_Person)
    if Age == 'quit':
        break
    Age = int(Age)
    if Age < 3:
        print("the ticket is free of cost")
    elif Age < 13:
        print("the ticket is $10")
    else:
        print("the ticket is $15")
