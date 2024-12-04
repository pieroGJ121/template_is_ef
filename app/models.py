from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "user"
    dni = Column(String, primary_key=True, index=True)
    
    # Relaciones
    bookings = relationship("Booking", back_populates="user")
    purchases = relationship("Purchase", back_populates="user")
    cancelations = relationship("Cancelation", back_populates="user")

class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, index=True)
    concert = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Relaciones
    bookings = relationship("Booking", back_populates="ticket")
    purchases = relationship("Purchase", back_populates="ticket")
    cancelations = relationship("Cancelation", back_populates="ticket")

class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer, ForeignKey("user.dni"), nullable=False)
    id_ticket = Column(Integer, ForeignKey("ticket.id"), nullable=False)
    status = Column(String, nullable=False)

    # Relaciones
    user = relationship("User", back_populates="bookings")
    ticket = relationship("Ticket", back_populates="bookings")

class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer, ForeignKey("user.dni"), nullable=False)
    id_reserva = Column(Integer, ForeignKey("booking.id"), nullable=False)
    id_ticket = Column(Integer, ForeignKey("ticket.id"), nullable=False)

    # Relaciones
    user = relationship("User", back_populates="purchases")
    ticket = relationship("Ticket", back_populates="purchases")
    booking = relationship("Booking")

class Cancelation(Base):
    __tablename__ = "cancelation"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer, ForeignKey("user.dni"), nullable=False)
    id_reserva = Column(Integer, ForeignKey("booking.id"), nullable=False)
    id_ticket = Column(Integer, ForeignKey("ticket.id"), nullable=False)

    # Relaciones
    user = relationship("User", back_populates="cancelations")
    ticket = relationship("Ticket", back_populates="cancelations")
    booking = relationship("Booking")