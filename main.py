from fastapi import FastAPI
from routes.auth import auth_router
from routes.outfit import outfit_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(outfit_router)