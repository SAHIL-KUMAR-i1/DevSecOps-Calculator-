from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0.0")


class Calculation(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def home():
    return {"message": "Calculator API is running"}


@app.post("/calculate")
def calculate(data: Calculation):
    operation = data.operation.lower().strip()

    if operation == "add":
        result = data.a + data.b
    elif operation == "subtract":
        result = data.a - data.b
    elif operation == "multiply":
        result = data.a * data.b
    elif operation == "divide":
        if data.b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = data.a / data.b
    else:
        raise HTTPException(
            status_code=400,
            detail="Operation must be add, subtract, multiply, or divide"
        )

    return {
        "a": data.a,
        "b": data.b,
        "operation": operation,
        "result": result
    }
