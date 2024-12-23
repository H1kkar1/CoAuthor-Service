from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db import db_helper

Base = db_helper.Base

chapter = Table(
    "chapters",
    db_helper.metadata_obj,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(255), nullable=False),
    Column('volume', Integer, default=1), #том/часть
    Column('ranobe_id', Integer, ForeignKey('ranobes.id'), nullable=False),
    Column('text', Text, nullable=False),

    Column('ranobe', relationship("Ranobe", back_populates="chapters"))
)

class Chapter:
    pass

db_helper.mapper_registry.map_imperatively(Chapter, chapter)