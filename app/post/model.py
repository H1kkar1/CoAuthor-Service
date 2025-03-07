from sqlalchemy import Column, String, Table, Uuid, Text, ForeignKey
from app.db import db_helper


post = Table(
    'post',
    db_helper.metadata_obj,
    Column('id', Uuid, nullable=False, primary_key=True),
    Column('title', String(1024), nullable=False),
    Column('description', Text(), nullable=False),
    Column('seeker', Uuid, nullable=False),
    Column('team', Uuid, nullable=True),
    Column('contacts', String(), nullable=True),
    Column('comments', Uuid, ForeignKey("chat.id", ondelete='CASCADE'), nullable=True),
)


class Post:
    """ Заглушка для маппинга sql моделей """
    pass


db_helper.mapper_registry.map_imperatively(Post, post)
