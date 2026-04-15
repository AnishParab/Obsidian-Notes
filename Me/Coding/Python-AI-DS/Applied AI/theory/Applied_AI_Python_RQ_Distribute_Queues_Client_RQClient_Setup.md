# RQ Installation
``` bash
pip install rq
```

---
# `/client/__init__.py`
- Makes this a package.

---
# `/client/rq_client.py`
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
