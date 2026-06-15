# Example 1

``` python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        super().hello()  # next in MRO — not necessarily A directly
        print("B")

class C(A):
    def hello(self):
        super().hello()
        print("C")

class D(B, C):
    def hello(self):
        super().hello()
        print("D")

D().hello()
```

**Output**
``` bash
A
C
B
D
```

**Trick to find the output**
- Opposite sequence to *MRO*

##### **MRO: `D → B → C → A`**
- `D.hello` calls `super()` → `B.hello`
- `B.hello` calls `super()` → `C.hello` (not `A` — MRO says C is next)
- `C.hello` calls `super()` → `A.hello`
- Each prints after `super()` returns — so output is bottom-up

---
###### Gotcha

- Every class in a multiple inheritance chain should use `super()` — skipping one breaks the chain

---
