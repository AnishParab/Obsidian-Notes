# Nested Objects
``` js
const company = {
  name: "TechCorp",
  employees: {
    alice: { role: "Dev", salary: 50000 },
    bob:   { role: "Ops", salary: 55000 }
  }
};

console.log(company.employees.alice.role); // "Dev"
```

---
