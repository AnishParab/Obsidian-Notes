# 1. Batch Processing
- **Definition:** Analytics performed on **data at rest** (stored data).  
- **Use Case:** Suitable for large volumes of historical data.  
- **Characteristics:**
  - Processes data in **chunks or batches**.
  - Typically has **higher latency**.
  - Optimized for **throughput over speed**.
- **Popular Technologies:**
  - Hadoop MapReduce
  - Apache Hive
  - Apache Pig
  - Apache Spark (batch mode)

---
# 2. Stream Processing
- **Definition:** Analytics performed on **data in motion** (real-time or near real-time data).  
- **Use Case:** Suitable for live data processing, event-driven applications.  
- **Characteristics:**
  - Processes data **as it arrives**.
  - Requires **low-latency, real-time processing**.
  - Often used for **monitoring, alerting, and real-time dashboards**.
- **Popular Technologies:**
  - Apache Kafka
  - Apache Flink
  - Apache Storm
  - Spark Streaming

---
