from pydantic import BaseModel
from fastapi import FastAPI


class Item(BaseModel):
    """Class for store `Item` models data.
    
    Examples:
        {
            "name": "Foo",
            "description": "An optional description",
            "price": 45.2,
            "tax": 3.5
        },
        {
            "name": "Foo",
            "price": 45.2
        }

    """

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """Endpoint for create `Item` model object.

    Example: 

    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
