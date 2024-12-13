import uvicorn
from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

if __name__ == '__main__':
    uvicorn.run("module_16_5:app", reload=True)