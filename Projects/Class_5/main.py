import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: 
    df = pd.read_csv('D:\AI_Project\Projects\Class_5\imdb_top_1000.csv')
except FileNotFoundError:
    print(Fore.RED + "Error: CSV file not found."); raise

genres = sorted({g.strip() for xs in df['Genre'].dropna().str.split(",") for g in xs})

def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
def senti(p): return "Positive 🙂" if p > 0 else "Negative 🙁" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre:
        d = d[d['Genre'].str.contains(genre, case=False, na=False)]
    if rating is not None:
        d = d[d['Rating'] >= rating]
    if d.empty:
        return "No suitable movies found. Try adjusting your criteria."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get('Overview')
        if pd.isna(ov):
            continue

        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n:
                break
    return out if out else "No suitable movies found. Try adjusting your criteria."
            
        

def show(recs, name):
    print(Fore.CYAN + f"\n{name}, here are your movie recommendations:")
    for i,(t,p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {t} - Sentiment: {p:2f} {senti(p)}")

def get_genre():
    print(Fore.GREEN + "Available genres:")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.GREEN}{i}. {g}")
    choice = input(Fore.GREEN + "Enter genre number (or press Enter to skip): ")
    if choice.strip() == "":
        return None
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(genres):
            return genres[idx]
        else:
            print(Fore.RED + "Invalid genre number. Skipping genre filter.")
            return None
    except ValueError:
        print(Fore.RED + "Invalid input. Skipping genre filter.")
        return None
    
def get_rating():
    choice = input(Fore.GREEN + "Enter minimum rating (0-10, or press Enter to skip): ")
    if choice.strip() == "":
        return None
    try:
        rating = float(choice)
        if 0 <= rating <= 10:
            return rating
        else:
            print(Fore.RED + "Rating must be between 0 and 10. Skipping rating filter.")
            return None
    except ValueError:
        print(Fore.RED + "Invalid input. Skipping rating filter.")
        return None
    
print(Fore.YELLOW + "Welcome to the Movie Recommender!")
name = input(Fore.YELLOW + "Please enter your name: ")
print(Fore.YELLOW + f"Hi {name}! Let's find some movies for you.")

genre = get_genre()
mood = input(Fore.GREEN + "Do you want only movies with non-negative sentiment? (y/n): ").strip().lower() == 'y'
print(Fore.YELLOW + "Analyzing sentiment for your preferences", end="")
mp = TextBlob(mood).sentiment.polarity
md = "Positive 😊" if mp > 0 else "Negative" if mp < 0 else "Neutral"
print(Fore.YELLOW + f" ({md})")

rating = get_rating()
print(Fore.YELLOW + "Finding recommendations", end="")
dots()
recs = recommend(genre=genre, mood=mood, rating=rating)

print(Fore.YELLOW + recs + "\n" if isinstance(recs, str) else "")

while True:
    a = input(Fore.GREEN + "Would you like to see the recommendations again? (y/n): ").strip().lower()
    if a == 'y':
        show(recs, name)
    elif a == 'n':
        print(Fore.YELLOW + "Thanks for using the Movie Recommender! Enjoy your movies!")
        break
    else:
        print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")