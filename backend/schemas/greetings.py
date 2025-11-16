from pydantic import BaseModel

class GreetResponse(BaseModel):
    message: str