# Decimal to Binary using Nested Loops

num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary equivalent: 0")
else:
    binary = ""

    while num > 0:          # Outer loop
        remainder = 0

        for i in range(1):  # Inner loop (nested)
            remainder = num % 2
            num = num // 2

        binary = str(remainder) + binary

    print("Binary equivalent:", binary)