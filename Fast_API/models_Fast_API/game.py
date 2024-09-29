from sqlalchemy import Column, Integer, String, VARCHAR
from backend.db import Base, SessionLocal


class Game(Base):
    __tablename__ = 'app_game'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR)
    cost = Column(Integer)
    size = Column(Integer)
    image = Column(VARCHAR)
    description = Column(String)
    reviews = Column(String)
