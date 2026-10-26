from fastapi import FastAPI

app = FastAPI(title="Customer Support Copilot")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
