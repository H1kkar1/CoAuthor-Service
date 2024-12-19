from typing import Annotated, Sequence, Type

from fastapi import Depends, HTTPException
from pydantic import UUID4
from rich import status
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.comment.model import Chat
from app.comment.service import delete_chat
from app.post.model import Post
from app.post.schema import PostWrite, PostUpdate, PostRead
import uuid


async def get_all_posts(
        session: AsyncSession,
) -> Sequence[PostRead]:
    query = select(Post)
    result = await session.scalars(query)
    return result.all()


async def get_post_by_id(
        session: AsyncSession,
        id=UUID4,
) -> Type[PostRead] | None:
    result = await session.execute(select(Post).filter(Post.id == id))
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return result.scalars().first()


async def create_post(
        session: AsyncSession,
        post_create: PostWrite,
) -> Post:
    try:
        id = uuid.uuid4()
        chat = Chat(id=id)
        session.add(chat)
        post = Post(**post_create.model_dump())
        post.id = id
        post.comments = id
        session.add(post)
        await session.commit()
        return post
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND, detail="Post not created")


async def update_post(
        session: AsyncSession,
        post_update: PostUpdate,
) -> str:
    query = update(Post).where(Post.id == post_update.id).values(
        description=post_update.description,
        contacts=post_update.contacts,
    )
    await session.execute(query)
    await session.commit()
    return "succesfuly update"


async def delete_post(
        session: AsyncSession,
        post_id: UUID4,
) -> str:
    try:
        await delete_chat(session=session, chat_id=post_id)
        query = delete(Post).where(Post.id == post_id)
        await session.execute(query)
        await session.commit()
        return "Пост успешно удалён"
    except Exception as e:
        return f"Произошла ошибка {e}"
