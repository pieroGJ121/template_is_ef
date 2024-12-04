from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Ticket(Base):
    __tablename__ == "ticket"
    id = Column(Integer, primary_key=True, index=True)
    concierto = Column(string)
    precio = Column(Integer)
    
class Reserva(Base):
    __tablename_- == "reserva"
    id = Column(Integer, primary_key=True, index=True)
    id_ticket = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    
class Compra(Base):
    __tablename == "compra"
    id = Column(Integer, primary_key=True, index=True)
    id_reserva = Column(Integer, primary_key=True, index=True)
    id_ticket = Column(Integer, primary_key=True, index=True)
    pay_method = Column(String)
    
class Cancelacion(Base):
    _tablename == "cancelacion"
    id = Column(Integer, primary_key=True, index=True)
    id_reserva = Column(Integer, primary_key=True, index=True)
    id_ticket = Column(Integer, primary_key=True, index=True)
    reason = Column(String)
    
    
    