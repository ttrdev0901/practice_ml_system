from lib2to3.pgen2.token import OP
from pydoc import describe
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Query
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return JSONResponse(content=item_dict)

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return JSONResponse(content={"item_id": item_id, **item.dict()})

@app.get("/items2/")
async def read_items(q: Optional[str] = Query(None, max_length=10, min_length=3, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.get("/items3/")
async def read_items(q: Optional[str] = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

@app.get("/items4/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results