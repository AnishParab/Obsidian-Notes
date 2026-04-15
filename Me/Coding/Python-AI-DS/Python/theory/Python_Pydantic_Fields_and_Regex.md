# Code
``` python
from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Anish Parab"],
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        le=1_000_000,
        description="Annual Salary in USD",
    )


class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        description="User email address",
    )

    phone: str = Field(
        ...,
        pattern=r"^(\+\d{1,3})?\d{10}$",
        description="Phone number with optional country code",
    )

    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )

    discounts: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage",
    )
```

---
###### NOTE
> TO know more about `regex` you can follow:
[Click here - regExr](https://regexr.com/)

---
