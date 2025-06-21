import random 
max_attempts = 7

for attempts in range(max_attempts):
    num = random.randint(1,100)
    user = int(input("Enter Your Guess: "))

    if num == user:
        print("Woo, You won the Game!")
        break
    elif num >= user:
        print("Chose higher number")
    else:
        print("Chose lower number")
else:
    print("You use your all attempts")
