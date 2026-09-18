# DevSecOps Calculator API

A simple FastAPI calculator API for the DevSecOps CI/CD lab.

## Operations

The `/calculate` endpoint supports:
- add
- subtract
- multiply
- divide

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive API documentation.

## Example request

```json
{
  "a": 10,
  "b": 5,
  "operation": "multiply"
}
```

Expected result:

```json
{
  "a": 10,
  "b": 5,
  "operation": "multiply",
  "result": 50
}
```
