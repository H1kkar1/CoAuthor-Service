from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.schemas import UserCreate, UserLogin

class UserService:
    """Сервис для работы с пользователями"""
    @staticmethod
    async def register(db: AsyncSession, user: UserCreate):
        """Метод для регистрации нового пользователя"""
        hashed_password = generate_password_hash(user.password)
        new_user = User(username=user.username, password=hashed_password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def login(db: AsyncSession, user: UserLogin):
        """Метод для авторизации пользователя"""
        result = await db.execute(select(User).filter(User.username == user.username))
        db_user = result.scalar_one_or_none()
        if db_user and check_password_hash(db_user.password, user.password): #Проверка пароля
            return db_user
        return None
