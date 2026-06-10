def print_mirrored_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
            
        for j in range(i):
            print("*", end="")

        print()

n = int(input("Enter the number of rows: "))
print_mirrored_triangle(n)