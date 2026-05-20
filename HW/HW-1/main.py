from textblob import TextBlob
from datetime import datetime

print("🎯 Welcome to Sentiment Spy!")

user_name = input("Enter your name: ").strip()

if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

positive_count = 0
negative_count = 0
neutral_count = 0

print(f"\nHello, {user_name}! 👋")
print("I'm here to analyze the sentiment of your messages.")
print("\nCommands:")
print("• history  → Show conversation history")
print("• stats    → Show sentiment statistics")
print("• reset    → Clear history")
print("• save     → Save history to a file")
print("• exit     → End the program\n")

while True:

    user_input = input("You: ").strip()

    if not user_input:
        print("⚠ Please enter a message.\n")
        continue

    # EXIT
    if user_input.lower() == "exit":
        print(f"\n👋 Exiting Sentiment Spy. Goodbye, {user_name}!")
        break

    # RESET
    elif user_input.lower() == "reset":
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0
        print("🗑 Conversation history has been reset.\n")
        continue

    # HISTORY
    elif user_input.lower() == "history":

        if not conversation_history:
            print("📭 No conversation history available.\n")

        else:
            print("\n📜 Conversation History:\n")

            for idx, data in enumerate(conversation_history, start=1):

                text = data["text"]
                polarity = data["polarity"]
                sentiment = data["sentiment"]
                timestamp = data["time"]

                emoji = (
                    "😊" if sentiment == "Positive"
                    else "😞" if sentiment == "Negative"
                    else "😐"
                )

                print(
                    f"{idx}. [{timestamp}] "
                    f"{text} | "
                    f"Polarity: {polarity:.2f} "
                    f"({sentiment}) {emoji}"
                )

            print()

        continue

    # STATS
    elif user_input.lower() == "stats":

        total = positive_count + negative_count + neutral_count

        if total == 0:
            print("📊 No stats available yet.\n")
            continue

        avg_mood = (
            (positive_count - negative_count) / total
        )

        print("\n📊 Sentiment Statistics:")
        print(f"😊 Positive Messages : {positive_count}")
        print(f"😞 Negative Messages : {negative_count}")
        print(f"😐 Neutral Messages  : {neutral_count}")
        print(f"🧠 Overall Mood Score: {avg_mood:.2f}\n")

        continue

    # SAVE TO FILE
    elif user_input.lower() == "save":

        with open("sentiment_history.txt", "w", encoding="utf-8") as file:

            for idx, data in enumerate(conversation_history, start=1):

                file.write(
                    f"{idx}. [{data['time']}] "
                    f"{data['text']} | "
                    f"Polarity: {data['polarity']:.2f} "
                    f"({data['sentiment']})\n"
                )

        print("💾 Conversation history saved to sentiment_history.txt\n")
        continue

    # SENTIMENT ANALYSIS
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0:
        sentiment_type = "Positive"
        emoji = "😊"
        positive_count += 1
        bot_reply = "Glad to hear that!"

    elif polarity < 0:
        sentiment_type = "Negative"
        emoji = "😞"
        negative_count += 1
        bot_reply = "I hope things get better soon."

    else:
        sentiment_type = "Neutral"
        emoji = "😐"
        neutral_count += 1
        bot_reply = "Got it!"

    timestamp = datetime.now().strftime("%H:%M:%S")

    conversation_history.append({
        "text": user_input,
        "polarity": polarity,
        "sentiment": sentiment_type,
        "time": timestamp
    })

    print(
        f"Sentiment: {sentiment_type} "
        f"(Polarity: {polarity:.2f}) {emoji}"
    )

    print(f"🤖 SpyBot: {bot_reply}\n")