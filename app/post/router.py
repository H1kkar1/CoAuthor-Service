from sqlalchemy import select
from typing import Annotated, Sequence
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import db_helper
from app.post.model import Post

from app.post.schema import PostRead, PostWrite


import app.post.service as service

post_router = APIRouter(
    prefix="/coauthor",
    tags=["CoAutor"],
)


@post_router.get(path="")
async def get_all_posts(
        session: AsyncSession = Depends(db_helper.sessionDep)
):
    result = await service.get_all_posts(session)
    return result


# @post_router.get("/post/{id}")
# async def get_post(
#         session: Annotated[
#             AsyncSession,
#             Depends(db_helper.sessionDep)
#         ],
#         id: Uuid,
# ) -> Post | None:
#     return session.get(SqlPost, id)


@post_router.post("", response_model=PostRead)
async def create_post(
        post: PostWrite,
        session: AsyncSession = Depends(db_helper.sessionDep),
):
    result = await service.create_post(
        session=session,
        post_create=post
    )
    return result
