import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Paris", "Tokyo", "New York"],
}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!",]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def recomend():
    print(Fore.CYAN + "TravelBot: (beaches, mountains, cities?)")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: I recommend visiting {suggestion}!")
        print(Fore.CYAN + "Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Great choice! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: No worries! Let's try another one.")
            recomend()
        else:
            print(Fore.RED + "TravelBot: I didn't understand that. Let's try again.")
            recomend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have recommendations for that. Please choose from beaches, mountains, or cities.")
        
    show_help()



def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?: ")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.GREEN + f"TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")


    print(Fore.GREEN + f"TravelBot: For a trip to {location} for {days} days, I recommend packing:")
    print(Fore.GREEN + "- Comfortable shoes")
    print(Fore.GREEN + "- Weather-appropriate clothing")
    print(Fore.GREEN + "- Travel-sized toiletries")
    print(Fore.GREEN + "- A good book or entertainment for the journey")
    
def tell_joke():
        print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.MAGENTA + "- Recommend destinations based on your preferences(say 'recommendation')")
    print(Fore.MAGENTA + "- Provide packing tips for your trip(say 'packing tips')")
    print(Fore.MAGENTA + "- Tell you a joke to brighten your day(say 'joke')")
    print(Fore.MAGENTA + "- Type 'exit' or 'bye' to end our chat\n")


def chat():
    print(Fore.CYAN + "TravelBot: Hi! I'm TravelBot, your travel assistant. How can I help you today?")
    name = input(Fore.YELLOW + "Your Name?: ")
    print(Fore.CYAN + f"TravelBot: Nice to meet you, {name}! What can I do for you?")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + "You: ").lower()

        if "recommendation" in user_input:
            recomend()
        elif "packing tips" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif user_input in ["exit", "bye"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        elif user_input in ["help"]:
            show_help()
        else:
            print(Fore.RED + "TravelBot: Sorry, I didn't understand that. Please try again.")
            show_help() 

if __name__ == "__main__":
    chat()