def shutdown():
    shut = input("do you want to shutdown the computer.(yes) or (no): ").lower()
    if shut=='yes':
        print("shutting down")
    elif shut=='no':
        print("abort shut down") 
    else:
        print("sorry")

shutdown()               
        