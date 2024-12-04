from pydantic import BaseModel
from typing import List


class Booking_schema(BaseModel):
    dni: String
    id_booking: int
    
class User_and_ticket_schema(BaseModel):
    dni: String
    id_ticket: int
