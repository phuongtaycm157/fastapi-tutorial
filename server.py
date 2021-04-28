from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
	return "Hello World!"

@app.get("/items/")
async def get_item(index: int = 0, step: int = 10):
  return items_db[index: index+step]

# Khai báo class kế thừa BaseModel, đóng vai trò là param cho request body
class Item(BaseModel):
  index: int
  step: Optional[int] = None

@app.post("/items/")
async def get_item(item: Item):
  return items_db[item.index: item.index+item.step]