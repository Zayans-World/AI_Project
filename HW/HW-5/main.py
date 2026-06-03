import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

# Load dataset
try:
    df = pd.read_csv(r'imdb_top_1000.csv')
except FileNotFoundError:
    print(Fore.RED + "Error: CSV file not found.")
    raise SystemExit

# Loading animation
def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print()

# Sentiment label
def senti(p):
    if p > 0:
        return "Positive 🙂"
    elif p < 0:
        return "Negative 🙁"
    else:
        return "Neutral 😐"

# Random movie recommender
def recommend(n=5):
    movies = df.dropna(subset=["Series_Title"])

    if len(movies) < n:
        n = len(movies)

    selected = movies.sample(n=n)

    recommendations = []

    for _, row in selected.iterrows():
        overview = row.get("Overview", "")

        if pd.isna(overview):
            overview = ""

        polarity = TextBlob(str(overview)).sentiment.polarity

        recommendations.append(
            (
                row["Series_Title"],
                row["Genre"],
                row["Rating"],
                polarity,
            )
        )

    return recommendations

# Display recommendations
def show(recs, name):
    print(Fore.CYAN + f"\n{name}, here are your random movie recommendations:\n")

    for i, (title, genre, rating, polarity) in enumerate(recs, 1):
        print(Fore.CYAN + f"{i}. {title}")
        print(Fore.GREEN + f"   Genre: {genre}")
        print(Fore.YELLOW + f"   Rating: {rating}")
        print(Fore.MAGENTA + f"   Sentiment: {polarity:.2f} {senti(polarity)}")
        print("-" * 50)

# Main program
print(Fore.YELLOW + "🎬 Welcome to the Random Movie Recommender!")

name = input(Fore.YELLOW + "Please enter your name: ").strip()

if not name:
    name = "Movie Lover"

print(Fore.YELLOW + f"\nHi {name}! Let's find some random movies for you.")

while True:
    print(Fore.YELLOW + "\nFinding random movies", end="")
    dots()

    recs = recommend()
    show(recs, name)

    choice = input(
        Fore.GREEN + "\nGenerate another set of random movies? (y/n): "
    ).strip().lower()

    if choice == "n":
        print(Fore.YELLOW + "\nThanks for using the Random Movie Recommender!")
        print(Fore.CYAN + "Enjoy your movies! 🍿")
        break
    elif choice != "y":
        print(Fore.RED + "Invalid input. Exiting program.")
        break