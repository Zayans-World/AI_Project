import requests

url = "https://baconipsum.com/api/?type=meat-and-filler&paras=1&format=json"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Here your random text: \n {fact_data[0]}")
    else:
        print("Failed to retrieve fact.")

while True:
    user_input = input("Press Enter to get a random technology fact or type 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()

    