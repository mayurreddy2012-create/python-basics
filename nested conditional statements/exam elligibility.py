medical_cause = input("do you have any medical cauuse?(y/n)")
if medical_cause == 'n':
    attendence = int(input("what is your attendence?"))
    if attendence >75:
        print("you are allowed to take an exam")
    else:
        print("you are not allowed")  
elif medical_cause == 'y':
    print("you are allowed to take an exam")      
else:
    print("invalid input")        