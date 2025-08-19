# Important Note By **Hitesh Choudhary**
- In any course of tailwind, we are taught to build mobile first.
- But, in reality many developers actually build for bigger screens.

> **NOTE :** **Hence, always worry about the smaller and above screens first**.

---
#  Mobile-First Approach in Tailwind CSS
- Tailwind CSS is **mobile-first by design**, which means:

> **You style for the smallest screens (mobile) by default**, then use responsive prefixes (`sm:`, `md:`, `lg:`, etc.) to apply styles at larger screen sizes.

---
# Why Mobile First?
- Most users browse from phones → optimize for that baseline.
- Progressive enhancement: Load faster, behave predictably.
- Keeps your CSS clean, scalable, and responsive by default.

---
# **Important Note**
> To style something for mobile, you need to use the unprefixed version of a utility, not the `sm: ` prefixed version.

---
