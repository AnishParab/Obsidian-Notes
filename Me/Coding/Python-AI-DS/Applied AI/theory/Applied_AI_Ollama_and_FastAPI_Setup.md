# FastAPI Docs
[FastAPI](https://fastapi.tiangolo.com/fastapi-cli/)

---
# Steps: FastAPI Setup
##### Step 1
- Install FastAPI.
##### Step 2
- Now you can do pip freeze.
##### Step 3
`server.py`
``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```
##### Step 4
- Run the code using `fastapi dev server.py`.

---
# Ollama on REST API's
[Docs](https://pypi.org/project/ollama/)
##### Step 1
``` bash
pip install ollama
```
##### Step 2
`server.py`
``` python
from ollama import Client
from fastapi import FastAPI, Body

app = FastAPI()

client = Client(
    host="http://localhost:11434",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(message: str = Body(..., description="The Message")):
    # Model name - Same as the one in OpenWebUI
    response = client.chat(
        model="gemma:2b", messages=[{"role": "user", "content": message}]
    )

    return {"response": response.message.content}
```

---
