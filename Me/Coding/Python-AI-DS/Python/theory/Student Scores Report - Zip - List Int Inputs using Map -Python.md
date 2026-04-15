# Problem Statement
**Student Scores Report**
- You’re building a simple student report generator that combines names and scores.  

**Tasks:**
1. Define a function generate_score_report that takes two lists — one with student names and one with their scores.
2. Use the zip() function to pair each student with their score.
3. Return a list of strings in the format "Name scored X marks"

---
# Code
``` python
def generate_score_report(names: list[str], scores: list[int]):
    score_report = []
    for name, score in zip(names, scores):
        score_report.append(f"{name} scored {score} marks")
    return score_report


names = input("Enter names of students (space separated).\n").split(" ")
scores = list(map(int, input("Enter scores of students (space separated).\n").split()))

score_report = generate_score_report(names, scores)
print(score_report)
```

---
