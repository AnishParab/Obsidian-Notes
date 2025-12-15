# Installation and API
- Install **requests** package.
- Add a minimal API call in `main.py`
	For now, just:
	- call the API,
	- get 1 question,
	- print the question text.
``` python
"""
This is a simple quiz game
"""

import os
import requests

API_URL = "https://quizapi.io/api/v1/questions"
API_KEY = os.getenv("QUIZAPI_KEY")  # we'll use an env var for the key


def fetch_one_question():
    if not API_KEY:
        print("Error: QUIZAPI_KEY environment variable is not set.")
        return None

    params = {
        "apiKey": API_KEY,
        "limit": 1,
        "category": "Linux",      # we can change this later
        "difficulty": "easy",     # we can change this later
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    if not data:
        print("No questions returned from API.")
        return None

    return data[0]  # first (and only) question


def run_quiz():
    print("Welcome to my computer quiz game")

    while (response := input("Do you want to play the quiz?\n").lower()) not in (
        "yes",
        "no",
    ):
        print("Please answer yes or no.")

    if response == "no":
        print("Exiting.")
        return
    else:
        print("Let's play...\n")

    # NEW: fetch a single question and just print the question text
    question = fetch_one_question()
    if question is None:
        return

    print("Question from API:")
    print(question["question"])


if __name__ == "__main__":
    run_quiz()
```

---
# Code Explanation
- **requests**: Make `HTTP` requests to API.
- **os**: Read environment variables like API Key.

#### API constants
``` python
API_URL = "https://quizapi.io/api/v1/questions"
API_KEY = os.getenv("QUIZAPI_KEY")
```

#### `fetch_one_question()`: **Encapsulates all networking**
- Validate the API key.
- Build the query parameters.
- Send a GET request.
- Handle network errors.
- Return one question dictionary, `params`.

---
