# Problem
**Student Grading System**
- You’re building an academic grading system.  

**Tasks:**
1. Define a function `calculate_grade(score)` that:
    - Returns “A” for score ≥ 90
    - “B” for ≥ 75
    - “C” for ≥ 60
    - “D” for ≥ 40
    - “F” otherwise
2. Define a second function `generate_student_report(name, score)` that:
    - Uses the first function to determine the grade.
    - Returns a report string like: "Aman has scored 80 and received grade B"
3. Write clean, reusable code using **functions**, **conditions**, and **string formatting**.

---
# Code
``` python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75 and score < 90:
        return "B"
    elif score >= 60 and score < 75:
        return "C"
    elif score >= 40 and score < 60:
        return "D"
    else:
        return "F"


def generate_student_report(name, score):
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"


print(generate_student_report("Aman", 100))
```

---
