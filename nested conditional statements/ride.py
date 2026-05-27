print("select your ride: ")
print("1. Bike")
print("2. Car")


choice = int(input("Enter your choice: "))

if choice == 1:
    print("what type of Bike?")
    print("1.scooty\n")
    print("2.scooter\n")

    choice2=int(input("Enter your choice2: "))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")

elif choice == 2:
    print("what type of car?")
    print("1.Sedan\n")
    print("2.XUV\n")

    choice3=int(input("Enter your choice3: "))
    if choice3 == 1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")  


else:
    print("wrong choice!")              
