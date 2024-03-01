from fastapi import APIRouter
from fastapi import Path
import json
from pydantic import BaseModel
from services.index import execute_dizionario
from services.index import Email


sendEmail_controller = APIRouter()

class emailReceiver(BaseModel):
    email: str

@sendEmail_controller.post("/sendEmail")
def send_parole(emailReceiver: emailReceiver):
    info = json.dumps(execute_dizionario.chiamata_parole())
    info_right = json.loads(info)
    email = Email(emailReceiver.email, info_right['Parole'], info_right['Definizione'], info_right['Sinonimi'])
    email.email_creation()
    email.send_email()
    return 1