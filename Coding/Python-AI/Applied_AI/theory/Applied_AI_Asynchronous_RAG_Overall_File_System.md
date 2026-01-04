# 1. FastAPI Server (`server.py`)
**Responsibilities**
- Exposes API endpoints
- Queues user requests for asynchronous processing

**Endpoints**
- `GET /`  
  Health check endpoint to verify the server is running.
- `POST /chat`  
  Accepts a user query and enqueues it for background processing via Redis Queue (RQ).

---
# 2. Main Entry Point (`main.py`)
**Responsibilities**
- Loads environment variables
- Starts the FastAPI application using `uvicorn`

**Details**
- Server runs on:
  - Host: `0.0.0.0`
  - Port: `8000`

---
# 3. Queue System (`client/rq_client.py`)
**Responsibilities**
- Configures Redis Queue (RQ) for background job processing

**Details**
- Connects to Redis/Valkey at:
  - Host: `localhost`
  - Port: `6379`
- Used by the API server to enqueue jobs

---
# 4. Worker (`queues/worker.py`)
**Responsibilities**
- Executes the RAG pipeline in the background

**`process_query()` Workflow**
1. Perform vector similarity search using **Qdrant**
2. Build contextual text from retrieved document chunks
3. Send context + user query to the LLM
4. Return the generated response

---
# Data Flow
1. User sends a request to `POST /chat`
2. FastAPI server enqueues the job using RQ
3. RQ worker picks up the job
4. Worker queries Qdrant for relevant document chunks
5. Retrieved context is combined with the user query
6. Context + query are sent to Gemini
7. Generated response is returned as the job result

---
# Infrastructure
### Containerized Services
Managed using **Docker Compose**:
- **Qdrant** — Vector database
- **Valkey** — Redis-compatible backend for RQ

---
