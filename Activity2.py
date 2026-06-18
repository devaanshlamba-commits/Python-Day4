actual_cost=float(input("Please enter the actual price of the product:"))
sell_amount=float(input("Please enter the sell amount of the product:"))

if(sell_amount>actual_cost):
   amount=sell_amount-actual_cost
   print("Total Profit={0}". format(amount))
else:
   print("No Profit")      