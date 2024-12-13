from fastapi import FastAPI, HTTPException, Request, Path, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/', response_class=HTMLResponse)
async def main_menu(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


@app.get(path='/user/{user_id}')
async def user_info(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("user.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int) -> User:
    if users:
        user_id = max(users, key=lambda m: m.id).id+1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def put_new_data(user_id: int, username: str, age: int) -> User:
    for eu in users:
        if eu.id == user_id:
            eu.username = username
            eu.age = age
            return eu
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    for i, eu in enumerate(users):
        if eu.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail='User was not found')


if __name__ == '__main__':
    uvicorn.run("module_16_5:app", reload=True)
