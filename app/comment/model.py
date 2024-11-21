from sqlalchemy import Column, Table, Uuid, String, Integer,ForeignKey
from app.db import mapper_registry

comment = Table(
    'comment',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('chat_id', Uuid, ForeignKey("chat.id"), nullable=False),
    Column('id_user', Uuid, nullable=False),
    Column('text', String(4096), nullable=False),
    Column('grade', Integer, nullable=False, default=0),
)

chat = Table(
    'chat',
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True, nullable=False),
)


class Comment:
    pass


class Chat:
    pass


mapper_registry.map_imperatively(Comment, comment)
mapper_registry.map_imperatively(Chat, chat)
