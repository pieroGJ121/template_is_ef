from pydantic import BaseModel
from typing import List


class Booking_schema(BaseModel):
    dni: str
    id_booking: int
    
class User_and_ticket_schema(BaseModel):
    dni: str
    id_ticket: int
