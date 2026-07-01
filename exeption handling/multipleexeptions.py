try:
    num1, num2 = eval(input("enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("result is",result)

except ZeroDivisionError:
    print("Division by zero is an error!!")    
except SyntaxError:
    print("Comma is missing.Enter numbers seperated by a comma like this 1, 2")
except:
    print("Wrong input") 
else:
    print("No exeptions") 
finally:
    print("This will execute no matter what")      

