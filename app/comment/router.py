from typing import Annotated, Sequence
from fastapi import APIRouter, Depends
from mako.parsetree import Comment
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import db_helper
from app.comment.schema import CommentBase, CommentUpdate
import app.comment.service as service

from pydantic import UUID4

comment_router = APIRouter(
    prefix="/comment",
    tags=["Comments"],
)


@comment_router.get(path="/all/{chat_id}")
async def get_all_comments(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
        chat_id: UUID4
) -> Sequence[CommentBase]:
    result = await service.get_all_comments_by_chat_id(session, chat_id)
    return result


@comment_router.get("/single/{comment_id}")
async def get_one_comment(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
        comment_id: int,
) -> CommentBase:
    print(comment_id)
    comment = await service.get_comment_by_id(session, comment_id)
    return comment


@comment_router.put("/")
async def update_comment(
        comment: CommentUpdate,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
) -> CommentUpdate:
    result = await service.update_comment(
        session=session,
        comment_update=comment,
    )
    return result


@comment_router.post("/")
async def create_comment(
        comment: CommentBase,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
) -> CommentBase:
    result = await service.create_comment(
        session=session,
        comment_create=comment,
    )
    return result


@comment_router.delete("/{id}")
async def delete_comment(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.sessionDep)
        ],
        comment_id:int,
) -> str:
    await service.delete_comment(session, comment_id)
    return ("Комментарий успешно удалён")
