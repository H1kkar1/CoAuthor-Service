from typing import Annotated, Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.comment.model import Chat
from app.db import db_helper
from app.post.model import Post
from app.post.schema import PostWrite, PostRead
import uuid


async def get_all_posts(
        session: AsyncSession = Depends(db_helper.sessionDep)
) -> Sequence[PostRead]:
    query = select(Post)
    result = await session.scalars(query)
    return result.all()


async def create_post(
        session: AsyncSession,
        post_create: PostWrite,
) -> Post:

    id = uuid.uuid4()
    chat = Chat(id=id)
    session.add(chat)
    post = Post(**post_create.model_dump())
    post.id = id
    post.comments = id
    session.add(post)

    await session.commit()
    return post
