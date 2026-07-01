bill = 0
eggs = 5
milk = 7
mop = 9
bucket = 6
# items = input("enter the items you want to buy.milk, mop, eggs or/and bucket?: ")
lst = ["eggs", "milk", "mop", "bucket"]
# if items in lst:
#     bill +=eval(items)
#     print(bill)

# cont = input("do you want to continue? yes/no:").lower()
for i in range(5):
    # if cont=='yes':
        items = input("enter the items you want to buy.milk, mop, eggs or/and bucket?: ")

        if items in lst:
            bill += eval(items)
            print(bill)
        else:
            print("invalid input")
        done = input("are you done shopping. y/n: ")
        if done=='y':
             print("you have only 10 rupee notes")      
             pay = int(input("how much do you want to pay?: ")) 
             if pay>=bill:
                change = pay-bill
                print("you need $",change) 
             elif bill>pay:
                print("you need to pay $",change) 
                break  
        elif done=='n':
            continue
        else:
             print("invalid input")




