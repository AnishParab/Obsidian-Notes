# What we are doing ?
![[fast_api_rag.excalidraw|500]]

---
# Installation
``` bash
pip install "fastapi[standard]"
```

---
# `server.py`
**server.py (API endpoints)**
- `/`: Root endpoint returning server status
``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Server is up  and running."}
```

---
# `main.py`
**main.py (Entry point)**
- Imports FastAPI app from server.py
- Loads environment variables from .env
- Starts uvicorn server on port 8000
``` python
from .server import app
from dotenv import load_dotenv
import uvicorn

load_dotenv()


def main():
    uvicorn.run(app, port=8000, host="0.0.0.0")


main()
```

**Running the file**:
``` bash
python -m <folder_name>.main
```

---
