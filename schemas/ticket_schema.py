from pydantic import BaseModel
from typing import Optional

class TicketSchema(BaseModel):
    name_event: str
    code: str
    location: str
    date: str
    price: float
    transaction_counter: int
    owner: int
