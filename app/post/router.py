from typing import Annotated, Sequence
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import db_helper
from app.post.schema import PostRead, PostWrite, PostBase, PostUpdate
import app.post.service as service

from pydantic import UUID4

post_router = APIRouter(
    prefix="/post",
    tags=["Post"],
)


@post_router.get(path="/")
async def get_all_posts(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
) -> Sequence[PostRead]:
    result = await service.get_all_posts(session)
    return result


@post_router.get("/{id}")
async def get_post(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
        id: UUID4,
) -> Annotated[PostRead, None]:
    post = await service.get_post_by_id(session, id)
    return post


@post_router.put("/{id}")
async def update_post(
        post: PostUpdate,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
):
    result = await service.update_post(
        session=session,
        post_update=post,
    )
    return result


@post_router.post("/")
async def create_post(
        post: PostWrite,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
) -> PostRead:
    result = await service.create_post(
        session=session,
        post_create=post,
    )
    return result


@post_router.delete("/{id}")
async def delete_post(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
        post_id: UUID4,
) -> str:
    result = await service.delete_post(session, post_id)
    return result

