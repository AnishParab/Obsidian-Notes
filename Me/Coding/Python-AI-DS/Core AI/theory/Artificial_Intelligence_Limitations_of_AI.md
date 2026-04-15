# Limitations of AI

- AI = optimization over data, not understanding
- Models learn patterns that minimize a loss function — no grounded, causal model of the world
##### **Objective-bound**
- Behavior driven entirely by the defined loss function
- No awareness of intent or correctness beyond it
- → reward hacking: exploits loopholes that satisfy the metric without satisfying the goal
##### **Data dependence**
- Learns only from the available data distribution
- → inherits bias, breaks under distribution shift
##### **Weak generalization**
- Mostly interpolates within seen data
- → poor out-of-distribution (OOD) performance
##### **No causality**
- Captures correlations, not cause-effect relationships
- Cannot reason about interventions ("what if X changed")
- → relies on spurious patterns that break under shift
##### **No grounding**
- Symbols not tied to physical reality or sensorimotor experience
- → hallucinations: plausible-sounding outputs detached from truth
##### **Limited reasoning**
- Struggles with long multi-step logical chains
- No stable internal world model
- → shallow or inconsistent reasoning
##### **No persistent memory**
- Stateless across sessions by default
- Does not learn continuously after deployment
- → no accumulation of experience
##### **Low robustness**
- Small input perturbations can cause large output shifts
- → vulnerable to adversarial inputs, unreliable on edge cases
##### **Hard to interpret**
- Decisions emerge from high-dimensional parameters
- Internal reasoning not directly accessible
- → difficult to debug, audit, or trust
##### **Security risks**
- Manipulable via inputs
- → prompt injection, data poisoning, model extraction
##### **No true creativity**
- Generates by recombining learned patterns
- No internal goals or intent
- → novelty is statistical recombination, not origination

---
