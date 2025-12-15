# `ask_question(question_data)`
``` python
def ask_question(question_data):
    """Show one multiple-choice question, get an answer, and return True/False."""
    print()
    print(question_data["question"])
    print()

    answers = question_data["answers"]
    correct_answers = question_data["correct_answers"]

    # Map letters (A, B, C, ...) to the answer keys (answer_a, answer_b, ...)
    option_map = {}  # "A" -> "answer_a", etc.

    for key, text in answers.items():
        if text is None:
            continue  # skip empty options like answer_e = null

        # key looks like "answer_a", "answer_b", ...
        letter = key.split("_")[-1].upper()  # "A", "B", ...

        print(f"{letter}: {text}")
        option_map[letter] = key

    if not option_map:
        print("This question has no valid answers.")
        return False

    # Get a valid user choice
    valid_letters = option_map.keys()

    user_choice = ""
    while user_choice not in valid_letters:
        user_choice = input("Your answer: ").strip().upper()
        if user_choice not in valid_letters:
            print("Please choose one of:", ", ".join(sorted(valid_letters)))

    chosen_key = option_map[user_choice]  # e.g. "answer_a"
    correct_flag_key = f"{chosen_key}_correct"  # e.g. "answer_a_correct"

    is_correct = correct_answers.get(correct_flag_key) == "true"

    if is_correct:
        print("Correct!")
        return True
    else:
        print("Wrong.")
        # Show correct option(s)
        correct_letters = []
        for letter, answer_key in option_map.items():
            flag_key = f"{answer_key}_correct"
            if correct_answers.get(flag_key) == "true":
                correct_letters.append(letter)

        if correct_letters:
            print("Correct answer(s):", ", ".join(sorted(correct_letters)))
        if question_data.get("explanation"):
            print("Explanation:", question_data["explanation"])
        return False
```

---