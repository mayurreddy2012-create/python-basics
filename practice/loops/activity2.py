
prevnum = 0
num = range(10)
for i in num:
    sum = i+prevnum
    print("current number", i,"previous number", prevnum,"sum", sum)
    prevnum = i

