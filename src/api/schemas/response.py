from pydantic import BaseModel

class RunResponse(BaseModel):
    success: bool
    test_name: str