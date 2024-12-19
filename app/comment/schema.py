from typing import Optional

from pydantic import BaseModel, UUID4


class CommentBase(BaseModel):
    """
        Модель данных для API

        - id: str | id комментария
        - chat_id: str | ID общего чата для поста
        - user_id: str | ID пользователя который оставил комментарий
        - text: str | Текст сообщения
        - grade: int | Оценки поста (лайки )
    """
    id: int
    chat_id: UUID4
    user_id: UUID4
    description: str
    grade: int


class CommentUpdate(BaseModel):
    id: int
    description: str


class ChatBase(BaseModel):
    """
        Модель данных для API
    """
    id: str


