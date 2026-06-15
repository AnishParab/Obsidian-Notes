# Problem Statement

- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
- You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
``` bash
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**
``` bash
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**
``` bash
Input: nums = [1,3,5,6], target = 7
Output: 4
```

---
# Code

``` python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

			if nums[mid] < target:
				lo = mid + 1
			else:
				hi = mid - 1
		
        return lo
```

---
**Time complexity**: $O(log n)$
**Space complexity**: $O(1)$

---
