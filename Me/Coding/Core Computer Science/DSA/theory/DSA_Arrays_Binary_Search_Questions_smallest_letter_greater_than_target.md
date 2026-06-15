# Problem Statement

- Given a characters array `letters` that is sorted in non-decreasing order and a character `target`, return the smallest character in the array that is larger than `target`
- Note that letters wrap around:
	- For example, if `target == 'z'` and `letters == ['a', 'b']`, the answer is `a`

- **Example**:
``` bash
Input: letters = ["c", "f", "j"], target = "a"
Output: "c"
```

- **Example**:
``` bash
Input: letters = ["c", "f", "j"], target = "c"
Output: "f"
```

- **Example**:
``` bash
Input: letters = ["c", "f", "j"], target = "z"
Output: "c"
```

- **Example**:
``` bash
Input: letters = ["c", "d", "f", "j"], target = "j"
Output: "c"
```

---
# Code

``` python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if letters[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return letters[lo % len(letters)]
```

---
**Time complexity**: $O(log n)$
**Space complexity**: O(1)

---
