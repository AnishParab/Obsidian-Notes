# Problem Statement

> Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc)
3. Print the updated message with emojis.

Examples:
Input:
	I love to code and drink tea when I'm happy.

Output:
	I love 💓 to code 💻 and drink tea 🧋when I'm happy 😁.

Bonus:
- Make it case-sensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

---
# Code

``` python
emoji_mapper = {
    "love": "💓",
    "happy": "😁",
    "code": "💻",
    "tea": "🧋",
    "music": "♪",
    "food": "🍕",
}

user_message = input("Enter your message: \n")

updated_words = []

for word in user_message.split():
    cleaned = word.lower().strip(".,!?")

    emoji = emoji_mapper.get(cleaned, "")

    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)

print("\n Enhaced message \n")
print(updated_message)
```

---
