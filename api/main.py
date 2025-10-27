from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
@app.get("/") def root(): return {"name":"AI SOW/Diagram API","ok":True}
class Req(BaseModel): text: str
@app.post("/api/requirements") def reqs(r: Req): return {"requestId":"REQ-1","eta":"instant"}
@app.get("/api/sow/{id}") def sow(id: str): return {"id":id,"status":"draft","sections":["Scope","Assumptions","Timeline"]}
