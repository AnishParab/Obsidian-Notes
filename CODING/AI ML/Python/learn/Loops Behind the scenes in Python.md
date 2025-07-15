# Iteration Tools
- for
- comprehension

**NOTE : Files have their own iterable tools.**

---
# Iterable Objects
- File
- List
- range
- Dict

---
# Response
- `__next__`

---
# Working
![[Loops Behind the Scenes.excalidraw|5000]]

---
# Code
``` python
myList = [1,2,3,4]
I = iter(myList)

print(I)
print(I.__next__())

# This Still Points to the first memory reference
# __next__ stores the next memory reference
print(I)
# Hence I still shows the memory reference it was showing before

```

---
# File vs Others
``` python
f = open('chai.py')
iter(f) is f
# Answer is True

myNewList = [1,2,3]
iter(myNewList) is myNewList
# Answer is False
```

---








