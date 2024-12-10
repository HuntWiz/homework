from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


def new_id_from_users():
    user_id = max(users['id'] for user in users) + 1 if users else 1
    return user_id


@app.get('/')
async def main_menu() -> dict:
    return {'message:': 'Здрасте'}


@app.get('/users')
async def get_users() -> dict:
    return (users)


@app.post('/user/{username}/{age}')
async def post_user(username: str, age: str) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    new_user = {f'{user_id}': f'Имя:{username}, возраст:{age}'}
    users.update(new_user)
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def put_new_data(user_id: str, username: str, age: str) -> str:
    description = f'Имя:{username}, возраст:{age}'
    if users[user_id]:
            users[user_id] = description
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    try:
        del users[user_id]
        return f'User {user_id} was deleted'
    except:
        raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run("module_16_3:app", reload=True)