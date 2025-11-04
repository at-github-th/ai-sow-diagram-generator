from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI SOW/Diagram API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class PlanIn(BaseModel):
    prompt: str

@app.get("/api/health")
def health():
    return {"ok": True, "name": "AI SOW/Diagram API"}

@app.post("/api/plan")
def plan(body: PlanIn):
    # return a deterministic mock so UI can render immediately
    return {
        "title": "Integration Plan",
        "summary": body.prompt,
        "steps": [
            {"id": 1, "name": "Scope & Constraints"},
            {"id": 2, "name": "Data Flows & APIs"},
            {"id": 3, "name": "Auth, Roles, Security"},
            {"id": 4, "name": "Testing & KPIs"},
        ]
    }
