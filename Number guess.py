import random 
max_attempts = 7

print("Welcome to the Number Guessing Game!")
num = random.randint(1, 100)

for attempts in range(max_attempts):
    user = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))

    if num == user:
        print("🎉 Wow! You won the Game!")
        break
    elif user < num:
        print("🔼 Choose a **higher** number.")
    elif user > num:
        print("🔽 Choose a **lower** number.")
    else:
        print("😵 Something unexpected happened?")
else:
    print(f"😔 You used all your {max_attempts} attempts. The correct number was {num}.")
