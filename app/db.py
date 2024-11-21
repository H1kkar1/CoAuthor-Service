from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from bestconfig import Config
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import registry

conf = Config('.env')

DATABASE_URL = conf.get("DB_URL")
print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]


mapper_registry = registry()