# AI SOW / Diagram Generator

**Stack:** Python (FastAPI)  
**API:** http://127.0.0.1:5106  
**Web:** http://localhost:5506

## Run (local)

### API
cd ai-sow-diagram-generator-native/api && python3 -m venv .venv && source .venv/bin/activate && pip install -U fastapi 'uvicorn[standard]' && uvicorn main:app --host 127.0.0.1 --port 5106 --reload

### Web (static tester)
cd ai-sow-diagram-generator-native/web && python3 -m http.server 5506

## Test
- **Ping:** curl -s http://127.0.0.1:5106 | jq .
- **Root:** GET /\n- **Plan:** POST /api/plan

