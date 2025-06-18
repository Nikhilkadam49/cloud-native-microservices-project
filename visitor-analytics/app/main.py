from fastapi import FastAPI, Request
from datetime import datetime
from typing import List
from app.models import Visit

app = FastAPI(title="Visitor Analytics Service")

visit_logs: List[Visit] = []

@app.post("/visit")
async def log_visit(request: Request):
    client_host = request.client.host
    user_agent = request.headers.get("User-Agent", "unknown")
    path = request.url.path

    visit = Visit(
        timestamp=datetime.utcnow(),
        ip=client_host,
        user_agent=user_agent,
        path=path
    )

    visit_logs.append(visit)

    if len(visit_logs) > 100:
        visit_logs.pop(0)

    return {"message": "Visit recorded."}

@app.get("/visits", response_model=List[Visit])
async def get_visits():
    return visit_logs
