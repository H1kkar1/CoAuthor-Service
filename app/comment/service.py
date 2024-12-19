from typing import Sequence

from fastapi import HTTPException
from pydantic import UUID4
from rich import status
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.comment.model import Chat
from app.comment.model import Comment
from app.comment.schema import CommentBase, CommentUpdate
import uuid


async def get_all_comments_by_chat_id(
        session: AsyncSession,
        chat_id: UUID4,
) -> Sequence[Comment]:
    """
    Получение всех комментариев для конкретного поста
    """
    query = select(Comment).where(Comment.chat_id == chat_id)
    result = await session.execute(query)
    return result.scalars().all()


async def get_comment_by_id(
        session: AsyncSession,
        comment_id: int,
) -> Comment:
    """
    Получечние 1 комментария
    Используется для редактирования или удаления
    """
    query = select(Comment).where(Comment.id == comment_id)
    result = await session.execute(query)
    return result.scalars().first()


async def get_chat(
    session: AsyncSession,
    id: UUID4,
) -> Chat:
    chat = await session.execute(select(Chat).where(Chat.chat_id == id))
    return chat


async def create_comment(
        session: AsyncSession,
        comment_create: CommentBase,
) -> CommentBase:
    """
    Создание комментария
    """
    try:
        id = uuid.uuid4()
        comment = Comment(**comment_create.model_dump())
        session.add(comment)
        await session.commit()
        return comment

    # TODO Сохранение комментариев в кеш а потом запись пакетом
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail="comment not created")


async def update_comment(
        session: AsyncSession,
        comment_update: CommentUpdate,
) -> CommentUpdate:
    """
    Изменение комментария
    """
    try:
        query = update(Comment).where(Comment.id == comment_update.id).values(
            id=comment_update.id,
            description=comment_update.description,
        )
        await session.execute(query)
        await session.commit()
        return comment_update
    except Exception as e:
        raise HTTPException(status_code=500, detail="something wrong")


async def delete_comment(
        session: AsyncSession,
        comment_id: int,
) -> str:
    """
    Удаление комментария
    """
    try:
        query = delete(Comment).where(Comment.id == comment_id)
        await session.execute(query)
        await session.commit()
        return f"Коментарий {id} успешно удалён"
    except Exception as e:
        return f"Exception {e}"


async def delete_messages_by_chat_id(
        session: AsyncSession,
        chat_id: UUID4,
):
    """
    Удаление всех коментариев из чата
    """
    try:
        query = delete(Comment).where(Comment.chat_id == chat_id)
        await session.execute(query)
        await session.commit()
        return "Комментариии успешно удаленны"
    except Exception as e:
        session.rollback()
        return "Давай по новой Саня, всё хуйня"


async def delete_chat(
        session: AsyncSession,
        chat_id: UUID4
):
    """Удаление конкретного комментария"""
    await delete_messages_by_chat_id(session, chat_id)
    await session.execute(delete(Chat).where(Chat.id == chat_id))
    await session.commit()