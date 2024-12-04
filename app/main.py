from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Ticket, Booking, Purchase, Cancelation
from app.schemas import Booking_schema, User_and_ticket_schema

app = FastAPI()

@app.post("/ticket/purchase")
def make_purchase(booking_base: Booking_schema, db: Session = Depends(get_db)):
    # Verificar que el usuario y el ticket existen
    user = db.query(User).filter(User.dni == booking_base.dni).first()
    booking = db.query(Booking).filter(Booking.id == booking_base.id_booking).first()
    if not user or not booking:
        raise HTTPException(status_code=404, detail="User or Ticket not found")

    # Registrar la compra
    new_purchase = Purchase(
        dni=booking_base.dni,
        id_reserva=id_booking,
        id_ticket=booking_base.id_ticket
    )
    db.add(new_purchase)
    db.commit()
    db.refresh(new_purchase)
    return {"message": "Purchase successful", "purchase": new_purchase}


@app.post("/ticket/cancelation")
def make_cancelation(booking_base: Booking_schema, db: Session = Depends(get_db)):
    # Verificar que la reserva y el ticket existen
    booking = db.query(Booking).filter(Booking.id == booking_base.id_booking).first()
    user = db.query(User).filter(User.id == booking_base.dni).first()
    if not booking or not user:
        raise HTTPException(status_code=404, detail="Booking or Ticket not found")

    # Registrar la cancelación y actualizar la reserva
    new_cancelation = Cancelation(
        dni=booking_base.dni,
        id_reserva=id_booking,
        id_ticket=booking_base.id_ticket
    )
    db.add(new_cancelation)
    ##AQUI VA EL PUT PARA ACTUALIZAR EL ESTADO
    db.commit()
    return {"message": "Cancelation successful", "cancelation": new_cancelation}

@app.post("/ticket/booking")
def make_booking(user_base: User_and_ticket_schema, db: Session = Depends(get_db)):
    # Verificar que el usuario y el ticket existen
    user = db.query(User).filter(User.dni == user_base.dni).first()
    ticket = db.query(Ticket).filter(Ticket.id == user_base.id_ticket).first()
    if not user or not ticket:
        raise HTTPException(status_code=404, detail="User or Ticket not found")

    # Registrar la reserva
    new_booking = Booking(
        dni = user_base.dni,
        id_ticket = ticket.id,
        status = "active"
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"message": "Booking successful", "booking": new_booking}
