# FastApi Libraries
from fastapi import APIRouter
from fastapi import Path


from services.index import execute_dizionario


dizionario_controller = APIRouter()

@dizionario_controller.get("/parole")
def send_parole():
    return execute_dizionario.chiamata_parole()