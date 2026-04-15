# Problem Statement
**Student Scores Report Generator**
You are building a **Student Scores Report Generator** for an educational system. The goal is to combine two separate lists—one containing student names and the other containing their corresponding marks—and generate a readable score report.

Tasks:
1. Take a list of **student names** as input (space-separated).
2. Take a list of **student marks** as input (space-separated integers).
3. Convert the marks input into integers using the **`map()`** function.
4. Use the **`zip()`** function to pair each student name with its corresponding mark.
5. For each student, generate a string in the format:
    ```
    "<Name> scored <Marks> marks"
    ```
6. Store all generated strings in a list.
7. Return the final list containing the score report for all students.

Expected Outcome
- The program should correctly pair names and marks.
- The output should be a list of formatted score statements.
- The logic should rely on `zip()` for combining lists and `map()` for integer conversion.

Example
**Input**
```
Names: Amit Riya John
Marks: 85 90 78
```
**Output**
```
['Amit scored 85 marks', 'Riya scored 90 marks', 'John scored 78 marks']
```

---
# Code
``` python
def generate_student_scores_report(names: list[str], marks: list[int]) -> list[str]:
    report = []
    for name, score in zip(names, marks):
        report.append(f"{name} scored {score} marks")
    return report


# Take inputs
names = input("Enter student names (space separated): ").split()
# map method
marks = list(map(int, input("Enter student marks (space separated): ").split()))

# Generate report
scores_report = generate_student_scores_report(names, marks)

print(scores_report)
```

---
