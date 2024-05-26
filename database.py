from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL bazasiga bog'lanish
engine = create_engine("postgresql://postgres:2004@localhost/delivery_db")
with engine.connect() as connection:
    query = text("SET client_encoding = 'utf8'")
    connection.execute(query)

Base = declarative_base()
session = sessionmaker
