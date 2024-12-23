from typing import Optional
from pydantic import BaseModel

class ChapterObject(BaseModel):
    title: Optional[str] = None
    ranobe: Optional[str] = None  # ranobe slug
    volume: Optional[int] = None
    text: Optional[str] = None

class ChapterSerializer(BaseModel):
    id: int
    title: str
    volume: int
    text: str

    class Config:
        orm_mode = True

class ChapterCreateSerializer(ChapterSerializer):
    ranobe: None

class ChapterFilterSerializer(BaseModel):
    ranobe: Optional[int] = None
    order_by: Optional[str] = None

class ChapterUpdateSerializer(ChapterSerializer):
    title: Optional[str] = None
    ranobe: Optional[int] = None
    text: Optional[str] = None

class ChapterShortenedSerializer(ChapterSerializer):
    text: None
