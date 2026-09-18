import uvicorn
import fastapi
from pathlib import Path
from src.api.schemas.reques import RequestSchema
from src.api.schemas.response import RunResponse

from src.application.parsers.yaml_parser import YamlParser
from src.workers.executor import TestExecutor  


app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"service": "DTAP", 
            "status": "running"}

@app.post("/run", response_model=RunResponse)
async def run(request: RequestSchema):
    parser = YamlParser()
    test = parser.load(Path(request.file))
    executor = TestExecutor()
    success = await executor.execute(test)
    return RunResponse(success=True, test_name=test.name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

