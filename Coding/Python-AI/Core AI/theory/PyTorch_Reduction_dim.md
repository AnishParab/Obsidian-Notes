# Reduction
- any operation that reduces a tensor to a smaller number of elements.

---
# Default Behavior: Collapse the entire Tensor
``` python
scores = torch.tensor([[10., 20., 30.], [5., 10., 15.]])

average_score = scores.mean()

print(f"Overall Mean: {average_score}")
```

---
# `dim` Let's you control which direction to collapse.
- Our scores tensor: 2 students, 3 assignments.

A simple rule for 2D tensors:

- dim=0: Collapses the rows. Operates Vertically.
- dim=1: Collapses the columns. Operates Horizontally.

---
# Calculating Averages by Dimension
``` python
scores = torch.tensor([[10., 20., 30.], [5., 10., 15.]])

# To get the average FOR EACH ASSIGNMENT, we collapse the student dimension (dim=0)
avg_per_assignment = scores.mean(dim=0)

# To get the average FOR EACH STUDENT, we collapse the assignment dimension (dim=1)
avg_per_student = scores.mean(dim=1)
```

---

| scores       | Assignment 1 | Assignment 2 | Assignment 3 | mean (dim=1) |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| Student 1    | 10           | 20           | 30           | 20           |
| Student 2    | 5            | 10           | 15           | 10           |
| mean (dim=0) | 7.5          | 15           | 22.5         |              |

---
