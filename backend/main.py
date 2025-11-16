from fastapi import FastAPI
from typing import Optional

from domain.greetings import build_greeting
from schemas.greetings import GreetResponse

app = FastAPI()

@app.get("/", response_model=GreetResponse)
def get_generic_greet() -> GreetResponse:
    return GreetResponse(message=build_greeting())

@app.get("/greet/{name}", response_model=GreetResponse)
def get_greet(name: Optional[str] = None) -> GreetResponse:
    return GreetResponse(message=build_greeting(name))