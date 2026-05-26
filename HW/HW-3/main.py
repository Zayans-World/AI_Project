import random
from colorama import Fore, Style, init


init(autoreset=True)

choices = ["rock", "paper", "scissors"]

print(Fore.CYAN + "========== Rock Paper Scissors Game ==========")

while True:
    user = input(
        Fore.YELLOW + "\nEnter rock, paper, or scissors: "
    ).lower()

    if user not in choices:
        print(Fore.RED + "Invalid choice! Try again.")
        continue

    computer = random.choice(choices)


    print(Fore.BLUE + f"\nYou chose: {user}")
    print(Fore.MAGENTA + f"Computer chose: {computer}")

    
    if user == computer:
        print(Fore.CYAN + "It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print(Fore.GREEN + "You win!")

    else:
        print(Fore.RED + "Computer wins!")

    again = input(
        Fore.YELLOW + "\nPlay again? (yes/no): "
    ).lower()

    if again != "yes":
        print(Fore.CYAN + "Thanks for playing!")
        break

