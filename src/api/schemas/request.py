from pydantic import BaseModel 

class RequestSchema(BaseModel):
    file: str