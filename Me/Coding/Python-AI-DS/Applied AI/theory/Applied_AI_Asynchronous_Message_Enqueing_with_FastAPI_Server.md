# `server.py`

- `/chat`: Accepts user queries, enqueues them for processing
- Uses Redis Queue to defer processing to workers
- Returns job ID for tracking
``` python
from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app = FastAPI()


@app.get("/")
def root():
    return {"status": "Server is up  and running."}


@app.post("/chat")
def chat(
    query: str = Query(
        ...,
        decription="The chat query of user",
    ),
):
    job = queue.enqueue(process_query, query)

    return {"status": "queued", "job_id": job.id}
```

---
