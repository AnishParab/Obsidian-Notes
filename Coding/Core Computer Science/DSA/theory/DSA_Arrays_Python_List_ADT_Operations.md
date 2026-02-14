# List — Abstract Data Type (ADT)

### `insert(x, i)`

**Goal:** add element `x` at position `i`.

**Effect:**
- New element is placed at index `i`
- Elements from `i` onward shift right by 1

---
### `remove(i)` / `remove(x)`

**Goal:** delete an element from the list.

**Common variants:**
- `remove(i)` → remove element at index `i`
- `remove(x)` → remove first occurrence of value `x`

**Effect:**
- After deletion, elements shift left to fill the gap

---
### `replace(i, x)`

**Goal:** overwrite element at index `i` with value `x`.

**Effect:**
- List length does **not** change
- Only the element at `i` is updated

---
## Typical List ADT API (for completeness)

- `get(i)` → returns element at index `i`
- `set(i, x)` → sets element at index `i`
- `size()` → number of elements
- `isEmpty()`
- `search(x)` → returns index / boolean
- `append(x)` / `pushBack(x)`
- `popBack()`

---
