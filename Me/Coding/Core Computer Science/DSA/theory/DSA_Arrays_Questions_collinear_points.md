# Problem Statement

- **Points** -> $P1 \ (x_1, y_1), \quad P2 \ (x_2, y_2), \quad P3 \ (x_3, y_3)$
- Tell whether all the points are collinear

###### Solution 1
- *Slope* of the points are equal.
- If $m_1 = \frac{y_2 - y_1} {x_2 - x_1}$ and $m_2 = \frac{y_3 - y_2} {x_3 - x_2}$ and $m_1 = m_2$
- then, points are colliear
**But**
- While solving $x_2 - x_1$ and $x_3 - x_2$ you might get '$0$' as the denominator
- Hence, $(y_2 - y_1) . (x_3 - x_2) = (x_2 - x_1) . (y_3 - y_2)$

###### Solution 2
- **Area of traingle** is `0`
- $\implies \ \frac{1}{2} \ (x_1 * (y_2 - y_3) + x_2 * (y_3 - y_1) + x_3 * (y_1 - y_2) = 0$

---
# Code: Approach 1

``` python
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9


def is_collinear_points(x1, x2, x3, y1, y2, y3):
    if (y2 - y1) * (x3 - x2) == (x2 - x1) * (y3 - y2):
        print("Given points are collinear")
    else:
        print("Given points are not collinear")


is_collinear_points(x1, x2, x3, y1, y2, y3)
```

---
# Code: Approach 2

``` python
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9


def is_collinear_points(x1, x2, x3, y1, y2, y3):
    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if area == 0:
        print("Given points are collinear")
    else:
        print("Given points are not collinear")


is_collinear_points(x1, x2, x3, y1, y2, y3)
```

---
**Time Complexity**: $O(1)$
**Space Complexity**: $O(1)$

---
