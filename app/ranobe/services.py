from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ranobe.models import Ranobe
from ranobe.schemas import RanobeCreate, RanobeUpdate
from typing import Sequence

async def get_all_ranobes(
        session: AsyncSession
) -> Sequence[Ranobe]:
    query = select(Ranobe)
    result = await session.scalars(query)
    return result.all()

async def get_ranobe_by_id(db: AsyncSession, id: int):
    query = select(Ranobe).filter(Ranobe.id == id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def create_ranobe(db: AsyncSession, ranobe: RanobeCreate) -> Ranobe:
    db_ranobe = Ranobe(
        title=ranobe.title,
        status=ranobe.status,
        creator_id=ranobe.creator_id,
        description=ranobe.description
    )
    db.add(db_ranobe)
    await db.commit()
    await db.refresh(db_ranobe)
    return db_ranobe

async def update_ranobe(db: AsyncSession, db_ranobe: Ranobe, ranobe_update: RanobeUpdate) -> Ranobe:
    for field, value in ranobe_update.dict(exclude_unset=True).items():
        setattr(db_ranobe, field, value)
    db.add(db_ranobe)
    await db.commit()
    await db.refresh(db_ranobe)
    return db_ranobe

async def delete_ranobe(db: AsyncSession, ranobe: Ranobe) -> None:
    await db.delete(ranobe)
    await db.commit()