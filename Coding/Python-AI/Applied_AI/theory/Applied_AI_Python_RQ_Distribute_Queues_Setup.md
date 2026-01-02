# RQ Installation
``` bash
pip install rq
```

---
# `/queues` : Consumer/Processor
- Consumes the Messages from the queues.
- [[Applied_AI_RAG_Worker_Orchestration]]

---
# `/client` : Producer
- Produces messages into the queue.
- `rq_client.py`
``` python
from redis import Redis
from rq import Queue

queue = Queue(
    connection=Redis(
        host="localhost",
        port=6379,
    )
)
```

> There's more in further chapters.

---
