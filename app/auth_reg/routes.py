from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas import UserCreate, UserLogin, UserOut
from app.services import UserService
from app.database import get_session
from app.models import User

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(User).filter(User.username == user.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Имя пользователя уже используется")

    db_user = await UserService.register(db, user) # Регистрация нового пользователя
    return db_user

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_session)):
    db_user = await UserService.login(db, user)
    if db_user:
        return {"message": "Успешная авторизация"}
    raise HTTPException(status_code=401, detail="Неверное имя пользователя и/или пароль")
