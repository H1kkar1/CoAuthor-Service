from pydantic import BaseModel, UUID4
from typing import Optional


class PostBase(BaseModel):
    """
        Модель данных для API

        - id: str | ID Поста для поиска со-авторов
        - title: str | Название поста
        - description: str | Основной текст поста
        - seeker: str | Человек который ищет со-автора
        - team: str | Команда которая ищет со-автора
        - contacts: str | Контактные данные для связи
    """
    title: str
    description: str
    seeker: Optional[UUID4]
    team: Optional[UUID4]
    contacts: str


class PostRead(PostBase):
    id: UUID4
    comments: UUID4


class PostUpdate(BaseModel):
    id: UUID4
    description: Optional[str]
    contacts: Optional[str]


class PostWrite(PostBase):
    pass
