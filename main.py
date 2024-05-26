from fastapi import FastAPI
from auth import auth_rooter
from order import order_rooter

app = FastAPI()
app.include_router(auth_rooter)
app.include_router(order_rooter)


@app.get('/')
async def root():
    return {"massage": "Asosiy sahifa"}
