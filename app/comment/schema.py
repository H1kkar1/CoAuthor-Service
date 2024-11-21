from pydantic import BaseModel


class Comment(BaseModel):
    id: str
    id_user: str
    text: str
    grade: int
    
