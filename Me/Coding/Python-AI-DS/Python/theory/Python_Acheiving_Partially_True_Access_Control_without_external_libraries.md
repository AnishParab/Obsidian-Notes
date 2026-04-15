> Nothing gives full C++/Java enforcement — Python trusts the developer

---
# Achieving true access control

- Read-only → `@property` with no setter
- Controlled write → `@property` + `@field.setter` with validation
> [[Python_property_Decorator_Getter_and_Setter]]

- Block runtime attribute addition → `__slots__`
> [[Python_slots_To_Stop_Attribute_Addition_at_Runtime]]
> We can still access the attributes, but can't add new attributes at runtime.


---
