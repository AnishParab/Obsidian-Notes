# Online Machine Learning

> **Continuously update model with incoming data (streaming setting)**

![[online_machine_learning.excalidraw|700]]


---
# Core Idea

- Data arrives sequentially: ( x_1, x_2, \dots )
- Model updates incrementally:  
$$
    \theta_{t+1} = \theta_t - \eta \nabla L(\theta_t; x_t)  
$$
- **Prediction + learning happen together**

---
# How It Works

- Train on **mini-batches / single samples**
- Update weights after each batch
- No full retraining cycle

**Implementation (example):**
- Incremental APIs (e.g., `partial_fit()` in scikit-learn)

---
# When to Use

- **Concept drift**
    - Data distribution changes over time
    - Example: e-commerce trends, user behavior
- **Streaming data**
    - Logs, sensors, financial transactions
- **Low-latency systems**
    - Need fast adaptation without retraining

---
# Advantages

- **Adaptive**
    - Continuously improves with new data
- **Efficient**
    - No need to retrain on full dataset
- **Real-time capability**
    - Suitable for dynamic environments

---
# **Learning Rate**

> Controls balance between **old knowledge vs new data**

- High $( \eta )$ → fast adaptation, risk of instability
- Low $( \eta )$ → stable, slow learning

**Failure modes:**
- Too high → forget past (catastrophic forgetting)
- Too low → cannot adapt to drift

---
# Disadvantages

- **Unstable updates**
    - Sensitive to noisy / bad data
- **Data quality risk**
    - Model learns from unverified inputs
- **Monitoring required**
    - Need:
        - drift detection
        - rollback mechanisms
        - validation pipelines
- **Harder debugging**
    - Model state continuously changing

> Online learning also faces challenges, such as the risk of overfitting to recent data and sensitivity to noisy or incomplete data.

---
# Real-World Examples

- Chatbots (continuous interaction learning)
- Fraud detection (new attack patterns)
- Recommendation systems (user behavior updates)

---
# Summary

- Online learning = **incremental, real-time model updates**
- Best for:
    - **non-stationary data (concept drift)**
- Trade-off:
    - **adaptability vs stability/control**

---
