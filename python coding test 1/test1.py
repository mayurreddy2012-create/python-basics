import random
print("guess a number from 1 to 100")
secret = random.randint(1, 100)
user_guess = int(input("enter a number which you think is the secret number: "))
lives = 5
while lives<=5:
    if user_guess==secret:
        print("you win!")
    elif user_guess>    