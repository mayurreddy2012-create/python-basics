print("enter marks obtained in 5 subjects")

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive 
avg = int(tot / 5)

validrange = range(0,101)

if avg not in validrange:
    print("invalid input")
elif avg in range(91,101):
    print("your grade is A1")
elif avg in range(81,91):
    print("your grade is A2")
elif avg in range(71,81):
    print("your grade is B1")               