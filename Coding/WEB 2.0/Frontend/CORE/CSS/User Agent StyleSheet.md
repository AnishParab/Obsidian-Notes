# What is User Agent Stylesheet ?
- The **User Agent Stylesheet** is the **default CSS** applied by the web browser to HTML elements when no custom styles are provided.
- Every browser (Chrome, Firefox, Safari, etc.) ships with its own default styles so that HTML elements have a basic, readable appearance even without CSS.

---
> **Different browsers** may have slightly different user agent styles — this is why **CSS resets** or **normalize.css** are used to make styles consistent across browsers.

---
---
# Key Points
- **Source:** Comes from the **browser**, not the developer or user.
- **Priority:** Lowest in the **cascade** (overridden by user styles and author styles).
- **Purpose:**
    - Ensure unstyled HTML is still readable and usable.
    - Provide a consistent base for form controls, headings, paragraphs, etc.
- **Examples:**
    - `<h1>` is bold and large by default.
    - `<a>` is blue and underlined by default.
    - `<ul>` has padding and bullet points.

---
