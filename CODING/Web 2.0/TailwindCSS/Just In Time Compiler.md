# JIT Compilation in TailwindCSS
- TailwindCSS only includes the **exact utility classes** your project actually uses, keeping the final CSS **small, lean, and production-ready**.
- Builds are **faster** because it doesn't have to generate and store thousands of unused classes ahead of time.
- **Optimized by design** – no need to manually purge unused CSS.

- **Supports arbitrary values**:  
    For example:
``` html
<div class="mt-[13px]">Custom margin</div>

```
- Instead of being limited to predefined spacing scales, you can directly write custom values like `mt-[13px]`.

- **Built into Tailwind by default** – no extra setup, configuration, or plugin required.

---

> The JIT engine compiles your CSS **on demand** as you build, giving you the power to write highly customized designs **without bloating your CSS**.

---
