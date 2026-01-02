# `pip freeze > requirements.txt`

- **Purpose**: Captures the exact versions of all installed Python packages.
- **Command**:
```bash
pip freeze > requirements.txt
```
    
- **What it does**:
    - Lists all packages in the current environment
    - Redirects the output to `requirements.txt`
        
- **Use case**:
    - Reproduce the same environment on another system
    - Share dependencies with others
	
- **Install from file**:
```bash
pip install -r requirements.txt
```
    
- **Important notes**:
    - Includes **direct + transitive dependencies**
    - Best used inside a **virtual environment**
    - Can become noisy for large projects

---
