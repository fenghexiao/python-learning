from fastapi import FastAPI
from tool_executor import execute_tool
from pydantic import BaseModel

app = FastAPI()


class ToolRequest(BaseModel):
    tool_name: str
    argument: str


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tools/execute")
def run_tool(request: ToolRequest):
    result = execute_tool(request.tool_name, request.argument)
    return result