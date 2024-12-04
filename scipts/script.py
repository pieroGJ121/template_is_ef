from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

# Configuración de la base de datos
DATABASE_URL = "postgresql://aaron:aaron546@localhost/software"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Faker para generar datos aleatorios
faker = Faker()

# Definimos los IDs iniciales considerando que ya existen 1,000 tuplas
initial_user_count = 1000
initial_ticket_count = 1000

# Insertar 1,000 usuarios nuevos
new_users = []
for i in range(1, 10):
    dni = f"DNI-{initial_user_count + i}"
    new_user = {
        "dni": dni
    }
    new_users.append(new_user)

# Inserción de nuevos usuarios con `text()`
for user in new_users:
    session.execute(
        text("""
        INSERT INTO "user" (dni)
        VALUES (:dni)
        """),
        {"dni": user["dni"]}
    )

# Insertar 1,000 tickets nuevos
new_tickets = []
for i in range(1, 10):
    ticket_id = initial_ticket_count + i
    concert = faker.company()
    price = random.randint(50, 300)
    new_ticket = {
        "id": ticket_id,
        "concert": concert,
        "price": price
    }
    new_tickets.append(new_ticket)

# Inserción de tickets usando `text()` y un bucle
for ticket in new_tickets:
    session.execute(
        text("""
        INSERT INTO "ticket" (id, concert, price)
        VALUES (:id, :concert, :price)
        """),
        {
            "id": ticket["id"],
            "concert": ticket["concert"],
            "price": ticket["price"]
        }
    )

# Confirmar cambios
session.commit()

print("1,000 nuevos usuarios y 1,000 nuevos tickets han sido insertados.")
