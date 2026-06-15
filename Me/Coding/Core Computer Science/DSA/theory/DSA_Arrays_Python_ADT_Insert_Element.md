# Insertion

``` python
arr = [2, 1, 8, 9, 12, 15, 11, 19]

# Insert an element 5 at index 2
arr.insert(2, 5)

print(arr)
```

**Output**:
``` text
[2, 1, 5, 8, 9, 12, 15, 11, 19]
```

---
# Conclusion

- Every element _after_ the index needs to be shifted towards the right, and similarly towards the left for elements _before_ the index.

> Time Complexity: **O(n)**.

---
