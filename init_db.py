from database import engine, Base
from models import User, Orders, Product

Base.metadata.create_all(bind=engine)
