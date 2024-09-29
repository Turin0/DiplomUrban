from pydantic import BaseModel


class CreateGame(BaseModel):
    title: str
    cost: float
    size: float
    description: str
    reviews: str
    image: str