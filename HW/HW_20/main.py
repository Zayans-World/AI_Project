import requests
import random

BASE_URL = "https://factfacts.com/api.php"

categories = {
    "1": ("Technology", "technology"),
    "2": ("Science", "science"),
    "3": ("Space", "space")
}


def get_fact(category=None):
    try:
        params = {}

        if category:
            params["cat"] = category

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            if data.get("ok"):

                fact = data["fact"]

                print("\nDid you know?")
                print(fact["text"])

                if "category" in fact:
                    print("Category:", fact["category"])

            else:
                print("No fact found.")
                print(data.get("error"))

        else:
            print("API Error:", response.status_code)

    except Exception as e:
        print("Connection error:", e)


while True:
    print("\nWelcome to the Fact Generator!")
    print("\nChoose a fact type:")
    print("1. Technology")
    print("2. Science")
    print("3. Space")
    print("4. Random Category")
    print("Q. Quit")

    choice = input("Enter choice: ").lower()

    if choice == "q":
        print("Goodbye!")
        break

    elif choice in categories:
        name, category = categories[choice]

        print(f"\n{name} Fact:")
        get_fact(category)

    elif choice == "4":
        name, category = random.choice(list(categories.values()))

        print(f"\nRandom Category: {name}")
        get_fact(category)

    else:
        print("Invalid choice.")