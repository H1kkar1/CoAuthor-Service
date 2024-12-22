from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    username: str
    password: str

class UserLogin(BaseModel):
    id: int
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
