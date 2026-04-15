> Nothing gives full C++/Java enforcement — Python trusts the developer

---
# **`attrs`**

```python
from attrs import define, field

@define
class Chai:
    flavor: str
    _strength: str = field(alias="_strength")
```

- Enforces types, validates on assignment
- Generates `__init__`, `__repr__`, `__eq__` automatically

---
# **`pydantic`**

```python
from pydantic import BaseModel, field_validator

class Chai(BaseModel):
    flavor: str
    strength: str

    @field_validator("strength")
    def validate_strength(cls, v):
        if v not in ["Mild", "Strong"]:
            raise ValueError("Invalid strength")
        return v

tea = Chai(flavor="Ginger", strength="Strong")
tea.flavor = "Lemon"  # allowed
tea.flavor = 123      # ValidationError — type enforced
```

- Runtime type enforcement on assignment
- Widely used in production — FastAPI is built on it

---
# **Bottom line**

- `attrs` → general OOP with enforced structure
- `pydantic` → data validation, API models, configs
- Neither gives true `private` — but both give type safety and validation that Python alone can't

---
