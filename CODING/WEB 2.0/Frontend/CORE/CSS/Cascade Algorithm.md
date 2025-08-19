# Cascade Algorithm
When multiple styles apply, CSS uses the following priority chain:
``` css
Origin → Importance → Specificity → Source Order
```

---
# Origin
CSS can come from three places:

| Origin Type   | Source                  | Priority |
| ------------- | ----------------------- | -------- |
| User Agent    | Browser default styles  | Lowest   |
| User Styles   | e.g. user custom styles | Medium   |
| Author Styles | Your CSS                | High     |

---
# Importance (`!important`)
Any rule marked `!important` overrides normal specificity and source order:
``` css
/* This will override all other color rules for <p> */
p {
  color: red !important;
}
```
- **Cons:** This can make debugging harder and create override hell.

---
# Specificity
- This applies to selectors for resolving conflicts between their priority order.

| Selector Type                                       | Points |
| --------------------------------------------------- | ------ |
| Inline styles                                       | 1000   |
| ID selectors (`#id`)                                | 100    |
| Class, attribute, pseudo-class (`.class`, `:hover`) | 10     |
| Type selectors (`div`, `h1`)                        | 1      |

#### Example:
``` html
<div id="header" class="title">Hello</div>
```

``` css
/* Specificity: 1 */
div {
  color: green;
}

/* Specificity: 10 */
.title {
  color: blue;
}

/* Specificity: 100 */
#header {
  color: red;
}
```
#### Result:
- `color: red;` applies due to highest specificity.

---
# Source Order
- Applies when two selectors have equal specificity.
- The one defined last in the stylesheet wins.
#### Example:
``` css
/* Both have specificity 1 */
p {
  color: green;
}

p {
  color: purple;
}
```
#### Result:
- `color: purple;` wins as it is defined last.

---
