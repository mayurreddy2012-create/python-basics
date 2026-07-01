try:
     age = int(input("enter your age: "))
     if age%2==0:
        print(age)
        print("even")
     else:
         print(age)    

except ValueError :
     print("you have entered the wrong data type")
     
        