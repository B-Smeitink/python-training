from typing import Union

from fastapi import FastAPI

app = FastAPI()

db = {1: "John Doe",
      2: "Sally Jones"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    try:
        return db[customer_id]
    except KeyError:
        return f"Index {customer_id} does not exist"
