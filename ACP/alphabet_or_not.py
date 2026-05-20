alphabet = ["a", "b", "c", "d","e", "f","g", "h","i", "j","k", "l","m", "n","o", "p","q", "r" ,"s", "t","u", "v","w", "x","y", "z"]
char = input("enter a character:  ").lower()
print(char)
if char in alphabet:
    print("it is an alphabet")
else:
    print("not an alphabet ")    
