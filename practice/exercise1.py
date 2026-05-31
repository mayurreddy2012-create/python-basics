def product_or_sum(num1, num2):

    product = num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
    

#test 1
result = product_or_sum(20, 30)    
print("the result = ", result)

#test 2
result = product_or_sum(40, 30)    
print("the result = ", result)

    