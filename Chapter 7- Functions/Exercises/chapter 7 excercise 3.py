##exercise 3:
def make_shirt(size,msg): 
    print("\nYour shirt size is "+ size + " " +"\nand it says "+msg)
x = "S"
y= "Cristiano Ronaldo"
make_shirt(x,y)
Shirt_size= str(input("\nEnter your shirt size:"))##S,M,L
Shirt_message = str(input("\nEnter the message you want to print:\n"))
make_shirt(Shirt_size,Shirt_message)