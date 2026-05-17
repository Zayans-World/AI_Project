print("Hello! I am an AI Bot. What is your name?")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today?")

mood = input().lower()

if mood == "good":
    print("That's great to hear! Keep up the positive vibes!")

elif mood == "bad":
    print("I'm sorry to hear that. Remember, it's okay to have bad days. Take care of yourself!")
else:
    print("I see. Sometimes it's hard to put our feelings into words.")

print(f"It was nice chatting with you, {name}. Have a wonderful day!")
