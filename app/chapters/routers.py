from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.chapters.schemas import ChapterSerializer, ChapterUpdateSerializer, ChapterCreateSerializer, ChapterObject
from chapters.services import create_chapter, update_chapter, get_chapter_by_id, get_chapters_list
from app.db import db_helper

chapter_router = APIRouter(
    prefix="/chapter",
    tags=["Chapters"],
)

@chapter_router.get("/{slug}/{pk}", response_model=ChapterSerializer)
async def get_chapter(slug: str, pk: int, db: AsyncSession = Depends(db_helper.get_session)):
    chapter = await get_chapter_by_id(db, pk=pk)
    if not chapter:
        raise HTTPException(status_code=404, detail="Глава не найдена")
    return chapter

@chapter_router.delete("/{slug}/{pk}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_chapter(slug: str, pk: int, db: AsyncSession = Depends(db_helper.get_session)):
    chapter = await get_chapter_by_id(db, pk=pk)
    if not chapter:
        raise HTTPException(status_code=404, detail="Глава не найдена")
    await db.delete(chapter)
    await db.commit()
    return {"detail": "Глава успешно удалена"}

@chapter_router.patch("/{slug}/{pk}", response_model=ChapterSerializer)
async def update_chapter_api(slug: str, pk: int, data: ChapterUpdateSerializer, db: AsyncSession = Depends(db_helper.get_session), user=Depends(IsChapterOwner)):
    chapter = await get_chapter_by_id(db, pk=pk)
    if not chapter:
        raise HTTPException(status_code=404, detail="Глава не найдена")
    chapter = await update_chapter(db, chapter, ChapterObject(**data.dict()))
    return chapter

@chapter_router.get("/{slug}", response_model=list[ChapterSerializer])
async def get_chapters(slug: str, db: AsyncSession = Depends(db_helper.get_session)):
    chapters = await get_chapters_list(db, novel_slug=slug)
    return chapters

@chapter_router.post("/{slug}", response_model=ChapterSerializer, status_code=status.HTTP_201_CREATED)
async def create_chapter_api(slug: str, data: ChapterCreateSerializer, db: AsyncSession = Depends(db_helper.get_session), user=Depends(IsChapterOwner)):
    chapter_object = ChapterObject(**data.dict(), novel=slug)
    chapter = await create_chapter(db, chapter_object)
    return chapter
