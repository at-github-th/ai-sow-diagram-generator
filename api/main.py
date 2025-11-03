from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI SOW/Diagram API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

API_TOKEN = "dev-token"

def check(token: Optional[str] = None):
    # TODO: plug real auth; for now allow if no token or matches
    if token is not None and token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

class SowReq(BaseModel):
    requirements: str

@app.get("/")
def root():
    return {"name":"AI SOW/Diagram API","ok":True}

@app.post("/api/sow")
def gen_sow(body: SowReq, _=Depends(check)):
    req = body.requirements.strip()
    sections = [
        {"title":"Scope","items":[req[:120] or "N/A"]},
        {"title":"Deliverables","items":["API endpoints","UI views","Docs"]},
        {"title":"Non-functionals","items":["Security","Scalability","Observability"]},
    ]
    return {"sow":{"sections":sections}}
