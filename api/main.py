from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
app=FastAPI(title="AI SOW/Diagram API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
TOKEN=os.getenv("API_TOKEN","dev-12345")
class Step(BaseModel): name:str; depends_on:list[str]=[]
class Plan(BaseModel): name:str; steps:list[Step]=[]
def check(token:str|None): 
    if token!=TOKEN: raise HTTPException(status_code=401, detail="unauthorized")
@app.get("/") 
def root(): return {"name":"AI SOW/Diagram API","ok":True}
@app.post("/api/plan")
def plan(p:Plan, x_api_key:str|None=Header(default=None)):
    check(x_api_key)
    seen=set(); order=[]
    def visit(s:Step):
        if s.name in seen: return
        for d in s.depends_on: 
            dd=next((x for x in p.steps if x.name==d), None)
            if dd: visit(dd)
        seen.add(s.name); order.append(s.name)
    for s in p.steps: visit(s)
    return {"order":order,"count":len(order)}
# uvicorn main:app --host 127.0.0.1 --port 5106 --reload
