count = 0
vowels = "aeiou"
str = input("enetr a string: ").lower()
for i in str:
    if i in vowels:
        count+=1
print("total number of vowels present in a sentence is",count)
