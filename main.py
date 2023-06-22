from fastapi import FastAPI
from enum import StrEnum
from random import randint


class ModelNames(StrEnum):
    """Enumeration of possible models names."""

    user="user"
    schema="schema"
    table="table"


app = FastAPI()


@app.get("/")
async def root():
    """Get default data."""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Get item data by id."""
    name = "NaMe"
    return {"id": item_id, "name": name}


@app.get("/models/{model_name}")
async def read_enum(model_name: ModelNames):
    """Get item data by id."""
    data = {"id": randint(1, 100)}
    if model_name == ModelNames.user:
        data.update([(model_name, "Data of model 1")])
    elif model_name == ModelNames.schema:
        data.update([(model_name, "Data of model 2")])
    elif model_name == ModelNames.table:
        data.update([(model_name, "Data of model 3")])
    return data


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Save path format of variable by `path` postfix."""
    return {"file_path": file_path}


@app.get("/items/query/")
async def items_query(skip: int = 0, limit: int = 10):
    """Get query parameters from url.
    
    Example: http://127.0.0.1:8000/items/?skip=1&limit=3

    """
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip : skip + limit]



@app.get("/bool/")
async def items_query(short: bool = False):
    """Get bool query parameters from url.

    Automatically convert any type of boolean parameters.
     
    Example:
        * http://127.0.0.1:8000/items/foo?short=0
        * http://127.0.0.1:8000/items/foo?short=True
        * http://127.0.0.1:8000/items/foo?short=true
        * http://127.0.0.1:8000/items/foo?short=on
        * http://127.0.0.1:8000/items/foo?short=yes
    
    or any other case variation (uppercase, first letter in uppercase, etc).

    """
    return {"result": "Short is enabled" if short else "Short is disabled"}
