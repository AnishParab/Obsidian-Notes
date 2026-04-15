# Era: 1970s–1980s — shift from general reasoning to domain-specific encoded knowledge

**Expert Systems**
- Encode human expert knowledge as explicit if-then rules
- Separate knowledge base (facts + rules) from inference engine

**Inference Mechanisms**
- Forward chaining — data-driven: start from known facts, fire rules until goal reached
- Backward chaining — goal-driven: start from goal, work backward to find supporting facts

**Examples**
- MYCIN — diagnosed bacterial infections using backward chaining; matched expert performance in narrow domain

**Why they failed to scale**
- Knowledge acquisition bottleneck: encoding expertise is slow and brittle
- No learning: rules hand-crafted, not derived from data
- Fragile outside defined rule scope

---
