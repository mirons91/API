from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field








class Data(BaseModel):
    number: int
    text: str


app = FastAPI()
# limiter = Limiter(key_func=get_remote_address)
# app = FastAPI()
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


dict_posts = {'number': int, 'text': str}


@app.get("/")
def read_main():
    return {"TDJ -> zadanie"}


@app.post("/items/", response_model=Data)
async def create_item(item: Data) -> Any:
    return item


@app.get("/items/{number}", response_model=list[Data])
async def read_items(number: int, text: str) -> Any:
        result = {}
        if isinstance(number, int) and isinstance(text, str):
            result.update({"number": number, "text": text})
        elif not isinstance(number, int) and not isinstance(text, str):
            ...
        elif not isinstance(number, int) and isinstance(text, str):
            result.update({"text": dict_posts.get('text')})
        elif isinstance(number, int) and not isinstance(text, str):
            result.update({"number": number})
        return {"valid": len(result), "invalid": 2 - len(result)}

# @app.post("/items/")
# def req(number: int, text: str):
#     dict_posts.update({'number': number, 'text': text})
#     return {'number': number, 'text': text}


# @limiter.limit("5/minute")
# async def homepage(request: Request):
#     return PlainTextResponse("test")

# @app.get("/items/{number}")
# def read_item():
#     number = dict_posts.get('number')
#     text = dict_posts.get('text')
#     result = {}
#     if isinstance(number, int) and isinstance(text, str):
#         result.update({"number": number, "text": text})
#     elif not isinstance(number, int) and not isinstance(text, str):
#         ...
#     elif not isinstance(number, int) and isinstance(text, str):
#         result.update({"text": dict_posts.get('text')})
#     elif isinstance(number, int) and not isinstance(text, str):
#         result.update({"number": number})
#     # return {"valid": len(result), "invalid": 2 - len(result)}
#     return {"valid": number, "invalid": text}

#
# @app.exception_handler(RateLimitExceeded)
# def rate_limit_exceeded_handler(request, exc):
#     return JSONResponse(
#         status_code=429,
#         content={"detail": "Rate limit exceeded"},
#     )

