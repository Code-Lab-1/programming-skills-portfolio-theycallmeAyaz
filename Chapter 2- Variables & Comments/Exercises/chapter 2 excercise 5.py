## Exercise 5: USB Shopper
#total cost of usb is noted as x
#total pounds left is noted as pounds_remaining
#cash_current means the amount of money with the shopper.
#cost_usb means cost of usb in pounds
cost_usb=6
cash_current=50
x = "total usbs bought = "
pounds_remaining="remaining amount of pounds left = "
print(x + str(int(cash_current/cost_usb)))
print(pounds_remaining + str(cash_current % cost_usb))
