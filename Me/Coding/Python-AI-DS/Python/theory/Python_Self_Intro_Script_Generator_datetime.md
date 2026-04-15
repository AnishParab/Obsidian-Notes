# Problem Statement

> Self - Intro Script Generator

Create a Python Scriptthat interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favourite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and reasonable format.

Example:
- If the user inputs:
	- Name: Anish
	- Age: 22
	- City: Goa
	- Profession: Software Developer
	- Hobby: Music

Your script might output:
``` text
"Hello! My name is Anish. I'm 22 years old and live in Goa. I work as a Software Developer and I absolutely enjoy playing music in my free time. Nice to meet you!"
```

Bonus:
- Add the current date to the end of the paragraph like:
``` text
"Logged on: 2026-03-24"
```
- Wrap the printed message with a decorative border of stars
``` text
(*)
```

---
# Code

``` python
import datetime

name = input("What is your name ?\n").strip()
age = input("How old are you ?\n").strip()
city = input("Which city do you live in ?\n").strip()
profession = input("What is your profession ?\n").strip()
hobby = input("What is your favourite hobby ?\n").strip()

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()

intro_message += f"\n Logged on: {current_date}"

border = "*" * 80

final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)
```

---
