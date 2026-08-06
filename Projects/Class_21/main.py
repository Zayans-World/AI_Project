import requests
#from config import HF_API_KEY
HF_API_KEY = "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"

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-interference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
TOPICS = ["Sports", "Technology", "Business", "Politics", "Health"]

def ask_hf(headline):
    payload = {
        "inputs": headline,
        "parameters": {"candidate_labels": TOPICS}
    }
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=10)
    if not r.ok:
        raise RuntimeError(f"Request failed with status code {r.status_code}: {r.text}")

    return r.json()

def best_topic(preds: list):
    best = max(preds, key=lambda x: x['score'])
    return best['label'], best['score']

def bar(score: float) -> str:
    pct = score * 100
    blocks = int(pct // 10)
    return "█" * blocks + " " * (10 - blocks)

def show(headline: str, preds: list):
    top_label, top_score = best_topic(preds)
    print("\n" + "=" * 60)
    print("??? News Topic Classifier ???")
    print("=" * 60)
    print("Headline:", headline)
    print(f"Best Topic: {top_label}")
    print(f"Confidence: {round(top_score*100,1)}% ({bar(top_score)})")
    print("\nTop 3 Guesses:")
    top3 = sorted(preds, key=lambda x: x['score'], reverse=True)[:3]

    for i, p in enumerate(top3, start=1):
        print(f"{i}. {p['label']:<11} - {round(p['score']*100,1)}% ({bar(p['score']*100,1)}%[{bar(p['score'])}])")
    print("=" * 60)


def main():
    print("Welcome to the News Topic Classifier!")
    print("Topics:", ", ".join(TOPICS))
    print("Type 'exit' to quit the program.")
    print("Enter a news headline to classify it into one of the following topics: ")
    

    while True:
        headline = input("\nEnter a news headline: ")
        if headline.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        if not headline.strip():
            print("Please enter a valid headline.")
            continue

        try:
            preds = ask_hf(headline)
            if isinstance(preds, list) and preds and "label" in preds[0]:
                show(headline, preds)
            else:
                print("Oops!! Unexpected response from the API.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

