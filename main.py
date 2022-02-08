import json

from enum import Enum
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional


app = FastAPI(debug=True)


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short:bool = False
):
    item = {"item_id": item_id, "owner": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has long description"}
        )
    return JSONResponse(content=item)


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return JSONResponse(content={"file_path": file_path})

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name":"Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q:Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return JSONResponse(content=item)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return JSONResponse({"model_name": model_name, "message":"Deep Learning FTW!"})
    
    if model_name == "lenet":
        return JSONResponse({"model_name": model_name, "message":"LeCNN all the images"})
    return {"model_name": model_name, "message": "Have some residuals"}

# ---------
# 順序: 
# /users/me -> "the current user"になる. meにはならない
# ---------
@app.get("/users/me")
async def read_user_me():
    return JSONResponse(content={"user_id": "the current user"})

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return JSONResponse(content={"user_id": user_id})