from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import db_helper
from app.ranobe.schemas import (
    RanobeCreate,
    RanobeUpdate,
    RanobeResponse,
)
from app.ranobe.services import create_ranobe, update_ranobe, delete_ranobe, get_ranobe_by_id

ranobe_router = APIRouter(
    prefix="/ranobe",
    tags=["Ranobes"],
)

@ranobe_router.post("/", response_model=RanobeResponse, status_code=status.HTTP_201_CREATED)
async def create_ranobe_endpoint(
    ranobe: RanobeCreate,
    db: AsyncSession = Depends(db_helper.get_session)
):
    ranobe = await create_ranobe(db, ranobe)
    return RanobeResponse(**ranobe.__dict__)

@ranobe_router.get("/id/{id}", response_model=RanobeResponse)
async def get_ranobe_by_id_endpoint(
    id: int,
    db: AsyncSession = Depends(db_helper.get_session)
):
    ranobe = await get_ranobe_by_id(db, id)
    if not ranobe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рунабэ не найдено!")
    return RanobeResponse(**ranobe.__dict__)

@ranobe_router.delete("/id/{id}", response_model=RanobeResponse)
async def delete_ranobe_by_id_endpoint(
    id: int,
    db: AsyncSession = Depends(db_helper.get_session),
):
    ranobe = await get_ranobe_by_id(db, id)
    if not ranobe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рунабэ не найдено!")
    await delete_ranobe(db, ranobe)
    return RanobeResponse(**ranobe.__dict__)

@ranobe_router.patch("/id/{id}", response_model=RanobeResponse)
async def update_ranobe_by_id_endpoint(
    id: int,
    ranobe_update: RanobeUpdate,
    db: AsyncSession = Depends(db_helper.get_session),
):
    ranobe = await get_ranobe_by_id(db, id)
    if not ranobe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рунабэ не найдено!")
    ranobe = await update_ranobe(db, ranobe, ranobe_update)
    return RanobeResponse(**ranobe.__dict__)
