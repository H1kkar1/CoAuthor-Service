import enum
from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db import db_helper

class Status(enum.Enum):
    CONTINUES = "continues"
    FINISHED = "finished"
    FROZEN = "frozen"

ranobe = Table(
    "ranobe",
    db_helper.metadata_obj,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String, unique=True, nullable=False),
    Column('cover', String, default="default_novel_cover.png"),
    Column('creator', String, nullable=False),
    Column('slug', String, unique=True, nullable=False),
    Column('status', Enum(Status, values_callable=lambda obj: [e.value for e in obj]), nullable=True, default=Status.CONTINUES),
    Column('description', Text, nullable=True),
    )

class Ranobe:
    pass

db_helper.mapper_registry.map_imperatively(Ranobe, ranobe)
