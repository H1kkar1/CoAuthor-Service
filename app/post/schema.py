from pydantic import BaseModel


class Post(BaseModel):
    id: str
    title: str
    description: str
    seeker: str
    team: str
    contacts: str
