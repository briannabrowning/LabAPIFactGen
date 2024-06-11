from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# create class
class Fact(BaseModel):
    id: int
    fact: str

# create list
fact_list = []

# get method for list
# endpoint url is /fact
@app.get("/fact")
async def main():
    return fact_list

# get method for retriving a fact by id
@app.get("/{id}")
async def get_fact_by_id(id):
    return next((f for f in fact_list if f.id == int(id)), None)

# post method for adding facts
@app.post("/add_fact/")
async def add_fact(fact: Fact):
    fact_list.append(fact)
    return fact