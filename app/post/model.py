from sqlalchemy import Column, String, MetaData, Table, Uuid, Text

metadata = MetaData()

post = Table(
    'post',
    metadata,
    Column('id', Uuid, nullable=False, primary_key=True),
    Column('title', String(1024), nullable=False),
    Column('description', Text(), nullable=False),
    Column('seeker', Uuid, nullable=False),
    Column('team', Uuid, nullable=True),
    Column('contacts', String(), nullable=True),
)