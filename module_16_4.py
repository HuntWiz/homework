from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def main_menu() -> dict:
    return {'message:': 'Здрасте'}


@app.get('/users')
async def get_users() -> list:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: int) -> User:
    user_id = max((u.id for u in users), default=0) + 1
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
    uvicorn.run("module_16_4:app", reload=True)
