def add(num1,num2):
    result = num1+num2
    return result
def subtract(num1,num2):
    result = num1-num2
    return result
def multiply(num1,num2):
    result = num1*num2
    return result
def divide(num1,num2):
    result = num1/num2
    return result
try:
    num1 = float(input("enter a number: "))
    num2 = float(input("enter another number: "))
    operator = input("which operator do you want?(+,-,*,/)")
    if operator=='+':
        print(add(num1,num2))
    elif operator=='-':
        print(subtract(num1,num2))
    elif operator=='*':
        print(multiply(num1,num2))
    elif operator=='/':
        print(divide(num1,num2))  
    else:
        print("invalid input")              

except ZeroDivisionError:
    print("you have calculated with zero ")
except ValueError:
    print("invalid data type")    
