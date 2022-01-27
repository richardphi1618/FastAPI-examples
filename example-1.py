from typing import Optional
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    unique_id: Optional[str]  # uuid generated when item logged
    user_id: str  # user id for user lookup later
    val: float  # value stored
    desc: Optional[str]  # user description of the item


@app.get("/items")
def list_items() -> dict:
    """
    see all items in list
    """
    return {"results": items}


@app.post("/items", status_code=201)
def create_item(body: Item) -> dict:
    """
    add item to list
    """
    unique_id = str(uuid4())
    print(unique_id)
    body.unique_id = unique_id
    items.append(body)
    return {"results": body}


@app.get("/items/")
def search_items_by_user_id(user_id: Optional[str] = None, max_results: Optional[int] = 10) -> dict:
    """
    Search for items based on user_id
    """
    if not user_id:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": items[:max_results]}

    results = [item for item in items if item.user_id == user_id]

    return {"results": list(results)[:max_results]}
