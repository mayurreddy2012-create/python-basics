number = int(input("enter the number: "))
temp_number = number
digit_count = 0
while temp_number > 0:
    digit_count +=1
    temp_number = temp_number // 10

if digit_count >=4:
    middle_position = digit_count // 2
    current_position = 0

    while number > 0:
        digit = number%10

        if current_position == middle_position:
            first_middle_digit = digit
        elif current_position == middle_position - 1:
            second_middle_digit = digit

        number = number // 10
        current_position += 1

    product = first_middle_digit*second_middle_digit

    print(f"\nproduuct of middle digits ({first_middle_digit}*{second_middle_digit}) = {product}")

else:
    print("\nit's not a 4-digit or more than 4-digit number!")                        