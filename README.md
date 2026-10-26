# Customer Support Copilot

A starter project for a customer support assistant. The current implementation
contains a minimal health endpoint and a sample ShopEasy shipping policy; the
copilot, retrieval pipeline, and dashboard are not implemented yet.

## Project folders

- `app/`: Python application code.
  - `api/`: HTTP API routes.
  - `channels/`: Future customer communication channels.
  - `agent/`: Future assistant and response logic.
  - `rag/`: Future document retrieval and grounding logic.
  - `db/`: Future database models and access code.
  - `core/`: Shared application configuration and utilities.
- `data/knowledge_base/`: Example support policies and other source documents.
- `evals/`: Future assistant evaluation cases.
- `tests/`: Automated tests.
- `dashboard/`: Reserved for a future support dashboard.

## Run the API

Activate the existing virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the development server from the project root:

```powershell
python -m uvicorn app.main:app --reload
```

The health endpoint is available at <http://127.0.0.1:8000/health> and returns
`{"status":"ok"}`.

## Run the test

With the virtual environment activated:

```powershell
python -m unittest discover -s tests -v
```

The test uses Python's standard-library `unittest` runner and FastAPI's
`TestClient`. Its `httpx` dependency is included in `requirements.txt`.

## Environment and database

`.env.example` lists the expected variable names without containing credentials.
Keep `.env` local and never commit real API keys or database passwords. To use
Docker Compose later, set `POSTGRES_DB`, `POSTGRES_USER`, and
`POSTGRES_PASSWORD` in your local `.env`; the Compose file requires these values
and stores database data in a named volume. No services are started by this
project setup.
