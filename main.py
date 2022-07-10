from fastapi import FastAPI
import uvicorn
from db.base import database
from endpoints import users

app = FastAPI(title='FastAPI template')
app.include_router(users.router, prefix='/users')

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get('/main')
async def main():
    return {'message': 'test text'}

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)