ch = input("Enter exactly one character: ")

# Validate input length
if len(ch) != 1:
    print("Error: Please enter exactly one character.")
else:
    ascii_value = ord(ch)

    print("ASCII value:", ascii_value)

    # Check character type
    if 'A' <= ch <= 'Z':
        print("Type: Uppercase Letter")

    elif 'a' <= ch <= 'z':
        print("Type: Lowercase Letter")

    elif '0' <= ch <= '9':
        print("Type: Digit")

    else:
        print("Type: Special Character")