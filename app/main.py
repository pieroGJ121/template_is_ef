from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app.models import User, Ticket, Booking, Purchase, Cancelation
from app.schemas import Booking_schema, User_and_ticket_schema
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ticket API", docs_url="/swagger")


@app.post("/ticket/purchase")
def make_purchase(booking_base: Booking_schema, db: Session = Depends(get_db)):
    # Verificar que el usuario y el ticket existen
    user = db.query(User).filter(User.dni == booking_base.dni).first()
    booking = db.query(Booking).filter(Booking.id == booking_base.id_booking).first()
    if not user or not booking:
        logger.error("Error en ejecucion")
        raise HTTPException(status_code=404, detail="User or Ticket not found")

    # Registrar la compra
    new_purchase = Purchase(
        dni=booking_base.dni,
        id_reserva=booking_base.id_booking,
        id_ticket=booking.id_ticket,
    )
    db.add(new_purchase)
    db.commit()
    db.refresh(new_purchase)
    logger.info("Exito en ejecucion")
    return {"message": "Purchase successful", "purchase": new_purchase}


@app.post("/ticket/cancelation")
def make_cancelation(booking_base: Booking_schema, db: Session = Depends(get_db)):
    # Verificar que la reserva y el ticket existen
    booking = db.query(Booking).filter(Booking.id == booking_base.id_booking).first()
    user = db.query(User).filter(User.dni == booking_base.dni).first()
    if not booking or not user:
        logger.error("Error en ejecucion")
        raise HTTPException(status_code=404, detail="Booking or Ticket not found")

    # Registrar la cancelación y actualizar la reserva
    new_cancelation = Cancelation(
        dni=booking_base.dni,
        id_reserva=booking_base.id_booking,
        id_ticket=booking.id_ticket,
    )
    db.add(new_cancelation)
    ##AQUI VA EL PUT PARA ACTUALIZAR EL ESTADO
    db.commit()
    logger.info("Exito en ejecucion")
    return {"message": "Cancelation successful", "cancelation": new_cancelation}


@app.post("/ticket/booking")
def make_booking(user_base: User_and_ticket_schema, db: Session = Depends(get_db)):
    # Verificar que el usuario y el ticket existen
    user = db.query(User).filter(User.dni == user_base.dni).first()
    ticket = db.query(Ticket).filter(Ticket.id == user_base.id_ticket).first()
    if not user or not ticket:
        logger.error("Error en ejecucion")
        raise HTTPException(status_code=404, detail="User or Ticket not found")

    # Registrar la reserva
    new_booking = Booking(dni=user_base.dni, id_ticket=ticket.id, status="active")
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    logger.info("Exito en ejecucion")
    return {"message": "Booking successful", "booking": new_booking}
