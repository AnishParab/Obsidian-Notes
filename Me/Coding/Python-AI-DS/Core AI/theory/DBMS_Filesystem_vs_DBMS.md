# Problems in a File System
##### Data Redundancy and Inconsistency
- **Data Redundancy** → Same data stored in **multiple files/locations**
- **Inconsistency** → Different copies of the same data **do not match**
**Cause**
- No centralized control over data updates

##### Difficulty in Accessing Data
- Data retrieval requires **custom programs**
- No **standard query mechanism**
**Impact**
- High development time for each new query

##### Data Isolation
- Data stored in **separate files** with different formats
- No unified view of data
**Impact**
- Difficult to combine and analyze data across files

##### Integrity Problems
- **Integrity constraints** (rules) are **not enforced centrally**
**Examples**
- Invalid values (e.g., negative salary)
**Cause**
- Constraints embedded in application code

##### Atomicity Problems
- **Atomicity** → A transaction should be **all-or-nothing**
**Problem**
- Partial updates may occur on failure
**Example**
- Money deducted but not credited

##### Concurrent-Access Anomalies
- Multiple users access/update data **simultaneously**
**Issues**
- Lost updates
- Inconsistent reads

##### Security Problems
- No fine-grained **access control**
**Impact**
- Unauthorized data access or modification

---
