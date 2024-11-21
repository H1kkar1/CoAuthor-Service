from typing import Annotated, Dict
from fastapi import APIRouter, Form
from app.db import SessionDep
from app.post.model import Post
from app.comment.model import Chat
from sqlalchemy import select, Uuid
from sqlalchemy.engine import Result
import uuid


post_router = APIRouter()


@post_router.get("/coauthor", response_model=None)
async def get_all_posts(
        session: SessionDep,
        page: int,
) -> list[Post]:
    query = select(Post)
    result: Result = await session.execute(query)
    posts = result.scalars().all()
    return list(posts)


@post_router.get("/coauthor/post/{id}", response_model=None)
async def get_post(
        session: SessionDep,
        id: Uuid,
) -> Post | None:
    return session.get(Post, id)


@post_router.post("/coauthor/create_post", response_model=None)
async def create_post(
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        seeker: Annotated[str, Form()],
        team: Annotated[str, Form()],
        contacts:  Annotated[list, Form()],
        session: SessionDep,
) -> dict[str, str]:
    id = uuid.uuid4().hex
    post = Post(
        id=id,
        title=title,
        description=description,
        seeker=seeker,
        team=team,
        contacts=contacts
    )
    chat = Chat(id=id)

    await session.add(chat, post)
    await session.commit()

    return {"Post id": id}
