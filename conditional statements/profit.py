actual_amount = float(input("enter the actual amount: "))
selling_price = float(input("enter the selling price: "))

if selling_price > actual_amount:
    amount = selling_price - actual_amount
    print("Total profit = {0}".
          format(amount))
else:
    print("no profit!!!")
       