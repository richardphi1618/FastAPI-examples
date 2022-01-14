from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = {}


class Item(BaseModel):
    user_id: int
    val: float
    desc: str


@app.get("/items")
def list_items():
    return items


@app.post("/items", status_code=201)
def create_item(body: Item):
    uniqueID = uuid4()
    print(uniqueID)
    items[str(uniqueID)] = body
    return body


@app.get("/items/{uniqueID}")
def get_item(uniqueID: str):
    print(f"\n************")
    print(uniqueID)
    print(items.keys())
    print(f"\n************")

    return items[uniqueID]
