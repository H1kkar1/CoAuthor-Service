from chapters.models import Chapter
from chapters.schemas import ChapterObject
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

async def create_chapter(db: AsyncSession, data: ChapterObject) -> Chapter:
    chapter = Chapter(
        title=data.title,
        ranobe_id=data.ranobe,
        text=data.text,
        volume=data.volume
    )
    db.add(chapter)
    await db.commit()
    await db.refresh(chapter)
    return chapter

async def update_chapter(db: AsyncSession, chapter: Chapter, data: ChapterObject) -> Chapter:
    for field, value in data.dict(exclude_unset=True).items():
        setattr(chapter, field, value)
    db.add(chapter)
    await db.commit()
    await db.refresh(chapter)
    return chapter

async def get_chapters_list(db: AsyncSession, ranobe_slug: str) -> list[Chapter]:
    result = await db.execute(select(Chapter).filter(Chapter.ranobe.has(slug=ranobe_slug)))
    chapters = result.scalars().all()
    if not chapters:
        raise ValueError(f'Рунобэ с slug - {ranobe_slug} нет')
    return chapters

async def get_chapter_by_id(db: AsyncSession, pk: int) -> Chapter:
    result = await db.execute(select(Chapter).filter(Chapter.id == pk))
    chapter = result.scalar_one_or_none()
    if not chapter:
        raise NoResultFound(f'Главы с id - {pk} нет')
    return chapter

async def get_chapter_list_by_slice(db: AsyncSession, slice: tuple[int], ranobe_slug: str) -> list[Chapter]:
    chapters = await get_chapters_list(db, ranobe_slug=ranobe_slug)
    return chapters[slice[0]:slice[1]]

async def delete_chapter_by_id(db: AsyncSession, pk: int) -> None:
    result = await db.execute(select(Chapter).filter(Chapter.id == pk))
    chapter = result.scalar_one_or_none()
    if not chapter:
        raise NoResultFound(f'Главы с id - {pk} нет')

    await db.delete(chapter)
    await db.commit()
