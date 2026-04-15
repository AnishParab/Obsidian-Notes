# `server.py`
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
        description="The chat query of user",
    ),
):
    # Enqueues process_query by passing the query as a parameter
    job = queue.enqueue(process_query, query)

    return {"status": "queued", "job_id": job.id}


@app.get("/job-status")
def get_result(
    job_id: str = Query(
        ...,
        description="Job ID",
    ),
):
    job = queue.fetch_job(job_id=job_id)

    if job is None:
        return {"error": "Job not found"}, 404

    return {
        "job_id": job.id,
        "status": job.get_status(),
        "created_at": job.created_at,
        "ended_at": job.ended_at,
    }
```

---
