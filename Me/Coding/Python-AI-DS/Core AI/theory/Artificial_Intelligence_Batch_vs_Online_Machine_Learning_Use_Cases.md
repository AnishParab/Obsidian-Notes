# Batch Learning

- Suitable when **data distribution is stable** (no significant concept drift).
- Training is done on **static historical datasets**; model remains fixed until retrained.
- Common use cases:
    - Image classification
    - Spam detection (in relatively stable environments)
    - Offline recommendation systems
- **Failure mode:** performance degrades when real-world data shifts.

---
# Online Learning

- Suitable when **data distribution changes over time** (concept drift present).
- Model updates **incrementally with incoming data**.
- Common use cases:
    - Finance (stock prediction, fraud detection)
    - Economics (demand forecasting)
    - Healthcare monitoring (patient vitals)
- **Failure mode:** sensitive to noise and adversarial data; requires stability mechanisms.

---
# Key Distinction

- Batch → **train once, deploy many**
- Online → **train continuously, adapt always**

---
