from fastapi import FastAPI
from pydantic import BaseModel,Field
from datetime import datetime
from db import CRUD

app = FastAPI(
    title= "Simple Todo API",
    description= " A simple API built using AppWrite's db",
    docs_url="/"
)

crud = CRUD()



class TodoCreateModel(BaseModel):
    title :str
    content: str
    date_added: str = Field(default=datetime.utcnow().isoformat())


class TodoUpdateModel(BaseModel):
    title :str
    content: str


@app.get('/todos')
async def get_all_todos():
    result = crud.list_todos()

    return result

@app.get('/todo/{todo_id}')
async def get_todo(todo_id:str):
    result = crud.retrieve_todo(todo_id)

    return result


@app.post('/todos',status_code=201)
async def create_todo(todo_data :TodoCreateModel):
    result = crud.create_todo(data= {
        'title' :todo_data.title,
        'content' :todo_data.content,
        'date_added':todo_data.date_added
    })

    return result


@app.patch('/todo/{todo_id}')
async def Update_todo(todo_id:str,update_data: TodoUpdateModel):
    result = crud.update_todo(
        todo_id=todo_id,
        data = {
            'title' : update_data.title,
            'content' :update_data.content
        }
    )

    return result


@app.delete('/todo/{todo_id}',status_code=204)
async def get_all_todos(todo_id:str):
    result = crud.delete_todo(
        todo_id=todo_id
    )

    return result

