from typing import Optional

def build_greeting(name: Optional[str] = None) -> str:
    if name:
        return f"hello {name.lower()}!"
    return "hello world!"