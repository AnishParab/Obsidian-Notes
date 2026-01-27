# Git is NOT a file tracker
Git tracks **snapshots of content**, not diffs.
Each commit is:
- a snapshot of the entire project
- plus references to parent commit(s)

---
# Git is a graph, not a timeline
- History is a **DAG**, not a straight line
- Branches are **pointers to commits**
- Merges create commits with **multiple parents**

> **Common misconception:**  
> “A branch is a copy of code.”  
> ❌ False. A branch is a movable pointer.

---
# Distributed by Design
### What “Distributed” Actually Means
- Every clone is a **first-class repository**
- No technical distinction between “server” and “client”
- Collaboration happens by **exchanging commits**

This enables:
- Offline commits
- Cheap branching
- Resilient workflows

---
