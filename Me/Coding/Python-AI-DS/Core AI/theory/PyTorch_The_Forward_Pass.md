# The Forward Pass
- This is the model's first guess.
- Hence it's gues is completely random.

---
# Simple Linear Regression
**y = XW + b**
- X is input data
- W is weight
- b is bias
- y is model's prediction.

- W and b are the two knobs our model can turn.
- Hence our purpose is to find the perfect values for them.

---
# Step 1: Creating our Data
- We will create a fake data that follows the line `y = 2x + 1` with some noise.

``` python
# Our batch of data will have 10 data points
N = 10
# Each data point has 1 input feature and 1 output value
D_in = 1
D_out = 1

# Create our input data X
X = torch.randn(N, D_in)

# Create our true target labels y by using the "true" W and b
# The true W is 2.0, the true b is 1.0
true_W = torch.tensor([2.0])
true_b = torch.tensor(1.0)

# Also add a little noise
y_true = X @ true_W + true_b + torch.randn(N, D_out) * 0.1
```

- The model will never see true_W or true_b.
- Its job is to discover them just by looking at X and y_true

---
# Step 2: The Parameter's: The Model's Brain
- We initialize the model's parameters with random values and turn on the magic switch.
``` python
# Initialize our parameters with random values and turn on the magic switch
W = torch.randn(D_in, D_out, requires_grad=True)
b = torch.randn(1, requires_torch=True)

print(f"Initial Weight W:\n {W}\n")
print(f"Initial Bias b:\n {b}")
```

- This is the model's initial hypothesis which is completely wrong, but it's a start.

---
# Step 3: The Implementation: From Math to Code
``` python
y_hat = X @ W + b

print(f"Prediction y_hat (first 3 rows):\n {y_hat[:3]}\n")
print(f"True Labels y_true (first 3 rows):\n {y_true[:3]}")
```

---
- We are terribly wronmg and hence need a **backward pass**.

---
