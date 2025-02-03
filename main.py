from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class News(BaseModel):
    title: str
    content: str | None = None
    views: int = 0

@app.post("/news/")
async def create_news(news: News) -> News:
    "endpoint to create news"
    return news


# @app.get("/news/{news_id}")
# async def read_news(news_id: int) -> dict[str, int | str]:
#     """
#     Endpoint returns news by id
#     """
#     return {"news_id": news_id}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/news/")
# async def read_item(skip: int = 0, limit: int = 10, q: str | None = None):
#     print(q)
#     return fake_items_db[skip: skip + limit]

# @app.get("/")
# async def root():
#     return {"message": "Hello World!"}       

