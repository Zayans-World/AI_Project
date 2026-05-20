from textblob import TextBlob

print(f" Welcome to Sentiment Spy!")

user_name = input("Enter your name: ")
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\nHello, {user_name}! I'm here to analyze the sentiment of your messages. Type 'exit' to end the conversation.\n")
print(f"Type  Reset , History , Exit")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        print("Please enter a message.")
        continue

    if user_input.lower() == "exit":
        print(f"Exiting Sentiment Spy. Goodbye! {user_name}👋")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print("Conversation history has been reset.")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print("No conversation history available.")
        else:
            print("\nConversation History:")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start = 1):
                if sentiment_type == "Positive":
                    emoji = "😊"

                elif sentiment_type == "Negative":
                    emoji = "😞"

                else:
                    emoji = "😐"

                print(f"{idx}. {text} - Polarity: {polarity:.2f} ({sentiment_type}) {emoji}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0:
        sentiment_type = "Positive"
        emoji = "😊"

    elif polarity < 0:
        sentiment_type = "Negative"
        emoji = "😞"

    else:
        sentiment_type = "Neutral"
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"Sentiment: {sentiment_type} (Polarity: {polarity:.2f}) {emoji}\n")
