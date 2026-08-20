from fastapi import FastAPI

from .routes import router as task_router

app = FastAPI(title="Fullstack Task System API", version="0.1.0")
app.include_router(task_router)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
