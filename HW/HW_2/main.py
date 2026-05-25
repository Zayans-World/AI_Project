import re
import random
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

# DESTINATIONS

destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Paris", "Tokyo", "New York"]
}

# JOKES

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

# MEMORY

history = []

# HELPER FUNCTIONS

def normalize_input(text):
    return text.strip().lower()

def save_history(command):
    history.append(command)

# RECOMMENDATION 

def recommend():
    print(Fore.CYAN + "TravelBot: Choose beaches, mountains, or cities")
    
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: I recommend visiting {suggestion}!")

        answer = normalize_input(input(Fore.CYAN + "Do you like it? (yes/no): "))

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy your trip to {suggestion}!")
        
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another recommendation.")
            recommend()

        else:
            print(Fore.RED + "TravelBot: Please answer with yes or no.")

    else:
        print(Fore.RED + "TravelBot: Invalid category.")

# PACKING TIPS 

def packing_tips():
    location = input(Fore.CYAN + "TravelBot: Where are you going?\nYou: ")
    days = input(Fore.CYAN + "TravelBot: How many days?\nYou: ")

    print(Fore.GREEN + f"\nPacking tips for {location} ({days} days):")
    print("- Comfortable shoes")
    print("- Weather-appropriate clothes")
    print("- Toiletries")
    print("- Phone charger")
    print("- Travel documents")

#JOKES 

def tell_joke():
    print(Fore.YELLOW + random.choice(jokes))

# NEW FEATURE 1: WEATHER

def weather_info():
    city = input(Fore.CYAN + "TravelBot: Which city?\nYou: ")

    fake_weather = random.choice([
        "Sunny ☀️",
        "Rainy 🌧️",
        "Cloudy ☁️",
        "Windy 🌬️"
    ])

    print(Fore.GREEN + f"TravelBot: The weather in {city} is currently {fake_weather}")

# NEW FEATURE 2: NEWS

def news_updates():
    news = [
        "New flight discounts available this summer!",
        "Tourism rates are increasing worldwide.",
        "A new beach resort opened in Bali.",
        "Travel safety guidelines updated for 2025."
    ]

    print(Fore.GREEN + "TravelBot News:")
    print("- " + random.choice(news))

# NEW FEATURE 3: TIME 

def local_time():
    city = input(Fore.CYAN + "TravelBot: Enter a city name:\nYou: ")

    current_time = datetime.now().strftime("%H:%M:%S")

    print(Fore.GREEN + f"TravelBot: Current local time in {city} is {current_time}")

# HISTORY

def show_history():
    if history:
        print(Fore.MAGENTA + "\nPrevious Commands:")
        for item in history:
            print("- " + item)
    else:
        print(Fore.RED + "No history found.")

# HELP MENU 

def show_help():
    print(Fore.MAGENTA + "\nI can help with:")
    print("- recommendation")
    print("- packing tips")
    print("- joke")
    print("- weather")
    print("- news")
    print("- time")
    print("- history")
    print("- help")
    print("- exit / bye\n")

#  MAIN CHATBOT 

def chat():

    print(Fore.CYAN + "TravelBot: Hello! I'm your travel assistant.")

    name = input(Fore.YELLOW + "Your name: ")

    print(Fore.GREEN + f"TravelBot: Nice to meet you, {name}!")

    show_help()

    while True:

        user_input = normalize_input(input(Fore.YELLOW + "\nYou: "))

        save_history(user_input)

        # Regex keyword matching

        if re.search(r"recommend|destination|trip", user_input):
            recommend()

        elif re.search(r"packing|bag|luggage", user_input):
            packing_tips()

        elif re.search(r"joke|funny", user_input):
            tell_joke()

        elif re.search(r"weather|temperature", user_input):
            weather_info()

        elif re.search(r"news|update", user_input):
            news_updates()

        elif re.search(r"time|clock", user_input):
            local_time()

        elif re.search(r"history|memory", user_input):
            show_history()

        elif user_input in ["help"]:
            show_help()

        elif user_input in ["bye", "exit"]:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break

        else:
            print(Fore.RED + "TravelBot: Sorry, I didn't understand.Can you repeat that again?")
            show_help()

# RUN PROGRAM

if __name__ == "__main__":
    chat()