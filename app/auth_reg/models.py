from sqlalchemy import Column, Integer, String, Table
from app.db import db_helper

Users = Table(
    'users',
    db_helper.metadata_obj,
    Column('id', Integer, primary_key=True, index=True),
    Column('username', String, unique=True, index=True, nullable=False),
    Column('password', String, nullable=False),
)

class Users:
    """ Заглушка для маппинга sql моделей """
    pass

db_helper.mapper_registry.map_imperatively(Users, users)