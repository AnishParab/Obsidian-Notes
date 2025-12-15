# Install
- **python-dotenv**

---
# Create `.env`
``` 
quiz_game/
├─ quiz_game/
│  ├─ main.py
│  └─ __init__.py
├─ .env
├─ requirements.txt
└─ README.md
```

---
# `.env`
``` text
QUIZAPI_KEY=YOUR_REAL_KEY_HERE
```

---
# Add `.env` to `.gitignore`
``` text
.env
```

---
# Load environment variables in `main.py`
``` python
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # NEW: loads .env into environment

API_URL = "https://quizapi.io/api/v1/questions"
API_KEY = os.getenv("QUIZAPI_KEY")
```

---
