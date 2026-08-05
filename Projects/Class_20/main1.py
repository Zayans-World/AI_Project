import requests
number = 2

url = f"http://numbersapi.com/{number}/math"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to retrieve fact.")

while True:
    user_input = input("Press Enter to get a random technology fact or type 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()