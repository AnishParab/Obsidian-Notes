# Batch vs Online Machine Learning

- **Batch Learning**
    - Train once on full dataset → deploy → only prediction
- **Online Learning**
    - Continuously update model while making predictions

| Aspect           | Batch Learning            | Online Learning                  |
| ---------------- | ------------------------- | -------------------------------- |
| Training pattern | Periodic (full dataset)   | Continuous (incremental updates) |
| Data requirement | Static dataset            | Streaming / sequential data      |
| Model state      | Fixed between retraining  | Continuously evolving            |
| Adaptability     | Low (delayed updates)     | High (real-time adaptation)      |
| Compute pattern  | Heavy, infrequent         | Light, frequent                  |
| Implementation   | Simpler                   | More complex                     |
| Stability        | High (controlled updates) | Lower (sensitive to new data)    |
##### Cost & Compute
- **Batch learning**
    - High cost per training cycle
    - Requires full data reprocessing
- **Online learning**
    - Lower cost per update
    - But continuous updates → cumulative cost
**Key insight:**
- Batch = **compute concentrated in chunks**
- Online = **compute distributed over time**

##### System-Level Trade-off
- **Batch**
    - Easier to debug, test, and validate
    - Suitable for stable environments
- **Online**
    - Handles **concept drift**
    - Requires monitoring, rollback, data validation

##### Adaptability
- Online learning models excel in adjusting to new data without the need for retraining from scratch.

##### Common Misconception
- “Batch requires fewer computations” → **Incorrect in total cost**
    - It requires **large periodic recomputation**
- “Online is always cheaper” → **Depends on update frequency and scale**


---
# Research Paper Analysis
[Refer this](https://www.sciencexcel.com/articles/To1vDXfK5R2wDpG4CnH1Jhp6DIoglGj80xe43WBe.pdf)

##### Batch Learning
- Accuracy -> 91.2%
- Prediction latencies -> 6s
- Memory usage -> 4GB
- CPU consumption -> 70%
- Training time -> 12h
##### Online Learning
- Accuracy -> 88.5%
- Prediction latencies -> 2s
- Memory usage -> 1.5GB
- CPU consumption -> 40%
- Training time -> 45min
- Greater adaptibility -> 90.3%

##### Predictive Maintenance Systems
- **Predictive maintenance (PdM)** uses sensor data and machine learning to predict equipment failures before they occur, reducing downtime and costs.
- **Machine learning** improves PdM by identifying complex patterns in historical and real-time data, enabling accurate failure forecasting.
- Different approaches like **supervised** and **unsupervised** learning help detect known failure patterns and anomalies.
- Two main paradigms are used: **batch learning (trained once on historical data, less adaptive)** and **online learning (continuously updated with new data, more flexible)**.
> Online learning is better suited for dynamic environments where equipment behavior changes over time.

---
