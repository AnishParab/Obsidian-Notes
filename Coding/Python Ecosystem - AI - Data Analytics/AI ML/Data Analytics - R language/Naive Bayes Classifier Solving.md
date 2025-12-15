- Apply statistical based algorithm to obtain the actual probabilities of each event to classify new tuple.

---
# Dataset

|  ID | Age    | Income | Student | Credit    | Buy-Computer |
| --: | ------ | ------ | ------- | --------- | :----------: |
|   1 | <=30   | High   | No      | Fair      |      No      |
|   2 | <=30   | High   | No      | Excellent |      No      |
|   3 | 31..40 | High   | No      | Fair      |     Yes      |
|   4 | >40    | Medium | No      | Fair      |     Yes      |
|   5 | >40    | Low    | Yes     | Fair      |     Yes      |
|   6 | >40    | Low    | Yes     | Excellent |      No      |
|   7 | 31..40 | Low    | Yes     | Excellent |     Yes      |
|   8 | <=30   | Medium | No      | Fair      |      No      |
|   9 | <=30   | Low    | Yes     | Fair      |     Yes      |
|  10 | >40    | Medium | Yes     | Fair      |     Yes      |
|  11 | <=30   | Medium | Yes     | Excellent |     Yes      |
|  12 | 31..40 | Medium | No      | Excellent |     Yes      |
|  13 | 31..40 | High   | Yes     | Fair      |     Yes      |
|  14 | >40    | Medium | No      | Excellent |      No      |

---
Total records = 14.  
Counts: `Yes = 9`, `No = 5`.  
$$
P(Yes) = 9/14 = 0.642857
$$
$$
P(No) = 5/14 = 0.357143.
$$
---
# Feature value sets
- Age ∈ {<=30, 31..40, >40} : **(k=3)**
- Income ∈ {High, Medium, Low} : **(k=3)**
- Student ∈ {Yes, No} : **(k=2)**
- Credit ∈ {Fair, Excellent} : **(k=2)**    

---
# Conditional counts by class (raw)

| Feature |     Value | Count given Yes | Count given No |
| ------- | --------: | --------------: | -------------: |
| Age     |      <=30 |               2 |              3 |
| Age     |    31..40 |               3 |              0 |
| Age     |       >40 |               2 |              2 |
| Income  |      High |               2 |              2 |
| Income  |    Medium |               3 |              3 |
| Income  |       Low |               4 |              0 |
| Student |       Yes |               6 |              1 |
| Student |        No |               3 |              4 |
| Credit  |      Fair |               6 |              3 |
| Credit  | Excellent |               3 |              2 |

---
# Compute P(X | C1) using Naive Bayesian Classification
- P(X1 | C1) = 