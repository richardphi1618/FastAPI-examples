from typing import Optional

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    if request.scope.get("root_path") == None:
        root_path = "none"
    else:
        root_path = request.scope.get("root_path")
    return {"Hello": "World", "root_path": root_path}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
