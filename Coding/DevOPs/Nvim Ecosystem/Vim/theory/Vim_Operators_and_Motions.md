# Operator–Motion Model

### Definition
```text
{operator} + {motion | textobject}
```

- **Operator**: action (`d`, `c`, `y`, etc.)
- **Motion/Textobject**: range definition (`w`, `e`, `$`, `}`, `iw`, etc.)

Example:
- `dw` → delete to start of next word
- `d4w` → delete over 4 words

---
# Count Semantics (General Rule)

```text
[count] applies to the entire command that follows
```

Formal shape:
```text
[count] + command
```

The `command` itself may include operators, motions, or text objects.

---
# Canonical Command Shapes

### 1) Count + Motion

```text
[count] + {motion}
```

- `5w` → move 5 words
- `9k` → move up 9 lines

---
# 2) Count + Operator + Motion/Textobject

```text
[count] + {operator} + {motion | textobject}
```

- `3dw` → delete 3 words
- `2d}` → delete 2 paragraph blocks

---
# 3) Count + Find Motion

```text
[count] + f{char}
```

- `f2` → jump to next `2`
- `3f2` → jump to 3rd next `2`

---
> **NOTE:** The commands "3dw" and "d3w" delete three words.  If you want to get really
		picky about things, the first command, "3dw", deletes one word three times;
		the command "d3w" deletes three words once.  This is a difference without a
		distinction.  You can actually put in two counts, however.  For example,
		"3d2w" deletes two words, repeated three times, for a total of six words.

---
# 4) Count + Insert/Append

```text
[count] + {insert/append} + {text}
```

- `3a!` → inserts `!!!`

---
# Motion Inclusivity (Critical Detail)

Motions define **range semantics**:
- **Exclusive**: end position not included
    - `w`, `b`, `(`, etc.
    - `dw` does **not** delete the first char of next word
- **Inclusive**: end position included
    - `e`, `$`, `f{char}`
    - `d2e` deletes through word end
    - `d$` deletes to and including line end

Vim decides inclusion based on the **motion**, not the operator.

---
