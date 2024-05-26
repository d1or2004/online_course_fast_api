from fastapi import APIRouter, status
from schemas import SignUpModel
from database import session, engine
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

auth_rooter = APIRouter(prefix="/auth")
session = session(bind=engine)


@auth_rooter.get('/')
async def auth():
    return {"massage": "Auth rooter"}


@auth_rooter.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bu emaildan oldin ro'yxatdan o'tkazilgan")

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bu username mavjud")

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),  # pip install werkzeug | shifirlash uchun
        is_active=user.is_active,
        is_staff=user.is_staff
    )
    session.add(new_user)
    session.commit()
    return new_user
