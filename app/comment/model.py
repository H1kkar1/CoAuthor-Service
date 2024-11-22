from sqlalchemy import Column, Table, Uuid, String, Integer,ForeignKey
from app.db import db_helper

comment = Table(
    'comment',
    db_helper.mapper_registry.metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('chat_id', Uuid, ForeignKey("chat.id"), nullable=False),
    Column('user_id', Uuid, nullable=False),
    Column('text', String(4096), nullable=False),
    Column('grade', Integer, nullable=False, default=0),
)

chat = Table(
    'chat',
    db_helper.mapper_registry.metadata,
    Column("id", Uuid, primary_key=True, nullable=False),
)


class Comment:
    """ Заглушка для маппинга sql моделей """
    pass


class Chat:
    """ Заглушка для маппинга sql моделей """
    pass


db_helper.mapper_registry.map_imperatively(Comment, comment)
db_helper.mapper_registry.map_imperatively(Chat, chat)
