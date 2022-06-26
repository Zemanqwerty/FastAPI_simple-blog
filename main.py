from fastapi import FastAPI
from pydantic import BaseModel
import psycopg


app = FastAPI()


DB_HOST = 'localhost'
DB_PASSWORD = '3864'
DB_PORT = 5432
DB_USER = 'zeman'
DB_NAME = 'sphere_ilo_01'


class Article(BaseModel):
    article_name:str
    article_text:str
    customer:str


@app.get('/users')
async def create_article():
    try:
        async with await psycopg.AsyncConnection.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT, host=DB_HOST) as conn: 
            async with conn.cursor() as cur:
                await cur.execute(
                    f"SELECT * FROM users;"
                )

                users_list = await cur.fetchall()

                return users_list
    except:
        pass