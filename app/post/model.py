from sqlalchemy import Column, String, Table, Uuid, Text, ForeignKey, ARRAY
from app.db import mapper_registry

post = Table(
    'post',
    mapper_registry.metadata,
    Column('id', Uuid, nullable=False, primary_key=True),
    Column('title', String(1024), nullable=False),
    Column('description', Text(), nullable=False),
    Column('seeker', Uuid, nullable=False),
    Column('team', Uuid, nullable=True),
    Column('contacts', ARRAY(String()), nullable=True),
    Column('comments', Uuid, ForeignKey('chat.id'), nullable=True),
)


class Post:
    pass


mapper_registry.map_imperatively(Post, post)
