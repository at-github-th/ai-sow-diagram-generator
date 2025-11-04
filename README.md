# AI SOW / Diagram Generator

Language: Python (FastAPI)

## How to run

API
```bash
cd ai-sow-diagram-generator-native/api && python3 -m venv .venv && source .venv/bin/activate && pip install -U fastapi 'uvicorn[standard]' && uvicorn main:app --host 127.0.0.1 --port 5106 --reload
```

Web
```bash
cd ai-sow-diagram-generator-native/web && python3 -m http.server 5506
```

Open http://localhost:5506

## Endpoints
- Root: GET /\n- Plan: POST /api/plan
