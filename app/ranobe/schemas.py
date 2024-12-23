from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RanobeBase(BaseModel):
    title: str
    status: str
    description: Optional[str] = None

class RanobeCreate(RanobeBase):
    creator: str

class RanobeUpdate(RanobeBase):
    title: Optional[str] = None

class RanobeResponse(RanobeBase):
    id: int
    slug: str
    cover: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class RanobeListResponse(BaseModel):
    id: int
    title: str
    slug: str
    cover: str
    status: str

    class Config:
        orm_mode = True

class RanobeFilter(BaseModel):
    order_by: Optional[str] = None
