from fastapi import FastAPI

app = FastAPI()

data_base = {
    1: "one",
    2: "two",
    3: "three",
}

@app.get("/", tags=["home-page"])
async def get_data():
    return data_base

from pydantic import BaseModel
class data_item(BaseModel):
    key: int
    value: str

@app.post("/post_data", tags=["post data"])
async def post_data(data:data_item):
    data_base[data.key] = data.value
    return f"database appended with data"


todos = [
    {
        "id": 1,
        "job": "Wake-up"
    },
    {
        "id": 2,
        "job": "Fresh-up" 
    },
    {
        "id": 3,
        "job": "GYM" 
    }
]

@app.get("/get_todo")
async def get_todo():
    return todos
    

@app.post("/post_todo")
async def post_todo(data:dict):
    todos.append(data)
    return f"todos updated with {data}"


@app.put("/post_todo/{id}")
async def update_todo(id: int, body: dict):
    for item in todos:
        if item["id"] == id:
            item["job"] = body["job"]
            return todos
    else:
        return todos
    
@app.delete("/delete_todo/{id}")
async def delete_todo(id:int):
    for item in todos:
        if item["id"]==id:
            todos.remove(item)
            return f"successfully removed data with id: {id}"
    else:
        return f"Can't delete data with id: {id}, not found"
    
    