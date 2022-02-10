from optparse import Option
from turtle import title
from typing import Optional
from unittest import result

from fastapi import FastAPI
from fastapi import Path
from fastapi import Body
from fastapi import Cookie
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from pydantic import Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = \
        Field(None, title="The description of the item", max_length=300)
    price: float
    tax: Optional[float] = \
        Field(..., gt=0, description="The price must be greater than zero")
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Item, 
    user: User, 
    importance: int = Body(..., gt=0),
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q":q})
    return results

@app.put("/items2/{item_id}")
async def update_item(item_id:int, item: Item = Body(..., embed=False)):
    results = {"item_id": item_id, "item":item}
    return results