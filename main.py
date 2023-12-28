import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from public.users import U_R
from public.companies import C_R
from datetime import datetime
from public.db import create_tables, index_builder
# создание таблиц и заполнение их начальными данными
create_tables()
index_builder()

app = FastAPI()
# включаем роутеры
app.include_router(U_R)
app.include_router(C_R)
# занесение информации о включении и выключении в log.txt
@app.on_event("startup")
def startup():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')
@app.on_event("shutdown")
def shutdown():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: End\n')

@app.get('/', response_class = HTMLResponse)
def index():
    return "<b> Привет, пользователь! </b>" 

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8000)