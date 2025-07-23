import random

def main():
    while True:
        user = input("Roll the Dice, Type (y or no): ")

        if user == "y":
            dice = random.randint(1, 6)
            print(f"Dice number is: {dice}")
        elif user == "no":
            print("Dice roller is closed")
            break
        else:
            print("Error Occurred: Unknown Command.")

main()
