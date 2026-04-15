# Model-Based vs Instance-Based Learning

| Aspect            | Model-Based Learning                     | Instance-Based Learning                      |
| ----------------- | ---------------------------------------- | -------------------------------------------- |
| Data Preparation  | Prepare data for training                | Prepare data for training                    |
| Training          | Train model to learn parameters/patterns | No explicit training (deferred to inference) |
| Storage           | Store trained model                      | No model; store entire dataset               |
| Generalization    | Happens before seeing new data           | Happens per query at inference time          |
| Prediction        | Use learned model                        | Use training data directly                   |
| Data Retention    | Can discard training data                | Must retain all training data                |
| Model Requirement | Requires defined model structure         | May not have explicit model                  |
| Storage Cost      | Low (parameters only)                    | High (full dataset stored)                   |

---

> Instance based models are also called as **lazy learners** as they do not do anything during model training.

---
