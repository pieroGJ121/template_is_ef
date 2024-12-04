import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Ticket, Booking, Purchase, Cancelation  # importa tus modelos
from app.database import Base  # asumiendo que `Base` se define en `app.database`

# Configuración de la sesión de base de datos para pruebas
@pytest.fixture
def db_session(postgresql):
    """Crea una sesión de base de datos para pruebas."""
    engine = create_engine(postgresql.dsn())
    Base.metadata.create_all(engine)  # Crea las tablas en la base de datos de pruebas
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)  # Limpia las tablas después de las pruebas

def test_user_creation(db_session):
    """Prueba de integración para la creación de un usuario."""
    # Crear un usuario de prueba
    new_user = User(dni="DNI-12345")
    db_session.add(new_user)
    db_session.commit()
    
    # Verificar que el usuario se haya guardado correctamente
    user = db_session.query(User).filter_by(dni="DNI-12345").first()
    assert user is not None
    assert user.dni == "DNI-12345"

def test_ticket_creation(db_session):
    """Prueba de integración para la creación de un ticket."""
    new_ticket = Ticket(id=1, concert="Concert A", price=100)
    db_session.add(new_ticket)
    db_session.commit()
    
    ticket = db_session.query(Ticket).filter_by(id=1).first()
    assert ticket is not None
    assert ticket.concert == "Concert A"
    assert ticket.price == 100

def test_booking_creation(db_session):
    """Prueba de integración para la creación de una reserva."""
    user = User(dni="DNI-12345")
    ticket = Ticket(id=1, concert="Concert A", price=100)
    db_session.add(user)
    db_session.add(ticket)
    db_session.commit()

    new_booking = Booking(dni="DNI-12345", id_ticket=1, status="confirmed")
    db_session.add(new_booking)
    db_session.commit()

    booking = db_session.query(Booking).filter_by(dni="DNI-12345", id_ticket=1).first()
    assert booking is not None
    assert booking.status == "confirmed"

def test_purchase_creation(db_session):
    """Prueba de integración para la creación de una compra."""
    user = User(dni="DNI-12345")
    ticket = Ticket(id=1, concert="Concert A", price=100)
    booking = Booking(dni="DNI-12345", id_ticket=1, status="confirmed")
    db_session.add(user)
    db_session.add(ticket)
    db_session.add(booking)
    db_session.commit()

    new_purchase = Purchase(dni="DNI-12345", id_reserva=1, id_ticket=1)
    db_session.add(new_purchase)
    db_session.commit()

    purchase = db_session.query(Purchase).filter_by(dni="DNI-12345", id_reserva=1, id_ticket=1).first()
    assert purchase is not None

def test_cancelation_creation(db_session):
    """Prueba de integración para la creación de una cancelación."""
    user = User(dni="DNI-12345")
    ticket = Ticket(id=1, concert="Concert A", price=100)
    booking = Booking(dni="DNI-12345", id_ticket=1, status="confirmed")
    db_session.add(user)
    db_session.add(ticket)
    db_session.add(booking)
    db_session.commit()

    new_cancelation = Cancelation(dni="DNI-12345", id_reserva=1, id_ticket=1)
    db_session.add(new_cancelation)
    db_session.commit()

    cancelation = db_session.query(Cancelation).filter_by(dni="DNI-12345", id_reserva=1, id_ticket=1).first()
    assert cancelation is not None
