
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def root(): return {"name":"AI Requirements → SOW/Diagram Generator API","ok":True}

class Req(BaseModel): text: str

@app.post("/api/requirements")
def reqs(r: Req): return {"requestId":"REQ-1","eta":"instant"}

@app.get("/api/sow/{id}")
def sow(id: str): return {"id":id,"status":"draft","sections":["Scope","Assumptions","Timeline"]}

@app.get("/api/diagrams/{id}")
def diag(id: str): return {"id":id,"mermaid":"graph TD; A-->B;"}
