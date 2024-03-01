from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.index import dizionario_controller, sendEmail_controller
from typing import Union

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(dizionario_controller)

app.include_router(sendEmail_controller)
