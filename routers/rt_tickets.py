from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schemas.ticket_schema import TicketSchema
from config.db import engine
from models.tickets import tickets
# Hashear password
# pip install werkzeug
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List


ticket = APIRouter()


@ticket.get("/")
def root():
    return {"message": "Hi, Im FastAPI with router"}

# SELECT
@ticket.get("/api/ticket", response_model=List[TicketSchema])
def get_tickets():
    with engine.connect() as conn:
        result = conn.execute(tickets.select()).fetchall()

        return result


# CREATE TICKET
@ticket.post("/api/ticket", status_code=HTTP_201_CREATED)
def create_ticket(data_ticket: TicketSchema):
    # con el entorno with hacemos que se cierre la conexion de la bd cuando se deje de utilizar
    with engine.connect() as conn:
        new_ticket = data_ticket.dict()
       
        conn.execute(tickets.insert().values(new_ticket))

        return Response(status_code=HTTP_201_CREATED)