# Machine Learning Challenges

- **Data Collection** — sourced via APIs or web scraping; quality and legality matter from step one

- **Insufficient / Unlabelled Data** — more data beats a better algorithm (Unreasonable Effectiveness of Data — Norvig et al.); labelling is expensive and bottlenecks supervised learning

- **Non-representative Data**
    - _Sampling Noise_ — small sample, random chance skews it.
	[[Data_Analysis_Sampling_Noise]]
    - _Sampling Bias_ — systematic flaw in how data was collected
	[[Data_Analysis_Sampling_Bias]]
    - Example: training a face detector only on light-skinned faces — model fails on darker skin tones not because of noise, but structural bias in collection

- **Poor Quality Data** — ~60% of ML work is data cleaning; missing values, outliers, and errors directly degrade model performance

- **Irrelevant Features** — Garbage In, Garbage Out; feature engineering / selection is critical — model can't un-learn noise

- **Overfitting** — model memorizes training data, fails to generalize; high variance [[Machine_Learning_Overfitting]]

- **Underfitting** — model too simple to capture the pattern; high bias [[Machine_Learning_Underfitting]]

- **Software Integration** — plugging a trained model into production systems is non-trivial; APIs, latency, versioning

- **Offline Learning / Deployment** — model trained once, then deployed; world changes, model doesn't → concept drift

- **Cost** — compute, storage, labelling, and maintenance add up fast; not just a one-time training cost

---
