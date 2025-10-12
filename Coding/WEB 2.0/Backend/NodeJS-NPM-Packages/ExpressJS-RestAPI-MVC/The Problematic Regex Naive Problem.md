- This algorithm builds a [[Nondeterministic Finite Automata]], which is a finite state machine where for each pair of state and input symbol there may be several possible next states.
- Then the engine starts to make transition until the end of the input.
- Since there may be several possible next states, a deterministic algorithm is used.
- This algorithm tries one by one all the possible paths (if needed) until a match is found (or all the paths are tried and fail).

---
# Example: `^(a+)+$`
![[RegDDOS.excalidraw|500]]

---
- For input, `aaaaX` there are 16 possible paths.
- But for, `aaaaaaaaaaaaaaaaX` there are 65536 possible paths, and the number is double for each additional `a`.
- This is an extreme case where the naïve algorithm is problematic, because it must pass on many paths to find a **non-matching input**.

---
# Backtracking
- The root-cause of the above example is in a Regex engine feature called **backtracking**.
- Unfortunately, most Regex engines today try to solve not only “pure” Regexes, but also “expanded” Regexes with “special additions”, such as back-references that cannot be always be solved efficiently (see **Patterns for non-regular languages** in [Wiki-Regex](https://en.wikipedia.org/wiki/Regular_expression) for some more details). So even if the Regex is not “expanded”, a naïve algorithm is used.

---
# Evil Regex
- A Regex pattern is called **Evil Regex** if it can get stuck on crafted input.
#### **Evil Regex contains**:
- Grouping with repetition
- Inside the repeated group:
    - Repetition
    - Alternation with overlapping

#### **Examples of Evil Regex**:
- `(a+)+$`
- `([a-zA-Z]+)*$`
- `(a|aa)+$`
- `(a|a?)+$`

---
# Attack
The attacker might use the above knowledge to look for applications that use Regular Expressions, containing an **Evil Regex**, and send a well-crafted input, that will hang the system. Alternatively, if a Regex itself is affected by a user input, the attacker can inject an **Evil Regex**, and make the system vulnerable.

---
# Risk Factors
![[Regex_Web.excalidraw|500]]
- Each layer uses **Regex**.
- An attacker can hang a WEB-browser (on a computer or potentially also on a mobile device), hang a Web Application Firewall (WAF), attack a database, and even stack a vulnerable WEB server.
- For example, if a programmer uses a Regex to validate the client side of a system, and the Regex contains an **Evil Regex**, the attacker can assume the same vulnerable Regex is used in the server side, and send a well-crafted input, that stacks the WEB server.

---


