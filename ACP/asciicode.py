ch = input("enter a character: ")
if len(ch) != 1:
    print("error. Try again")
else:
   ASCII_value = ord(ch) 
   print("The ascii value is", ASCII_value ) 

if 'A'<=ch<='Z':
    print("Uppercase") 
elif 'a'<=ch<='z':
    print("lowercase") 
elif '0'<=ch<='9':
    print("digit") 
else:
    print("special")         
      
