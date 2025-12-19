# Problem Statement
**Function Types**
- You're building a **Function Behavior Analyzer** to showcase different types of Python functions in action. Implement the following:

1. **Pure Function**
    - Write a function `pure_add(a, b)` that takes two integers and returns their sum.
    - It should not rely on or modify any external state.
2. **Impure Function**
    - Define a global variable `counter`.
    - Implement `impure_increment()` that increases the counter and returns its value.
3. **Recursive Function**
    - Implement `factorial_recursive(n)` that returns the factorial of a given number using recursion.
    - Handle base case correctly (e.g., `factorial_recursive(0) = 1`).
4. **Lambda Function with** `**map()**`
    - Write a function `square_list(nums)` that uses a lambda inside `map()` to return a new list with the squares of the numbers in the input list.

---
# Code
``` python
# Pure function
def pure_add(a, b):
    return a + b


counter = 0


# Impure function
def impure_increment():
    global counter
    counter += 1
    return counter


print(counter)


# Recursive function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Lambda function
def square_list(nums):
    return list(map(lambda x: x * x, nums))


print(pure_add(1, 2))
print(impure_increment())
print(factorial_recursive(4))
print(square_list([1, 2, 3]))
```

---
