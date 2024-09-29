from typing import Annotated
from sqlalchemy import insert, select, delete
from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from models_Fast_API.game import Game
from schemas import CreateGame

router_main = APIRouter(prefix='', tags=['main'])
templates = Jinja2Templates(directory='templates')


@router_main.get('/main')
async def main_page(request: Request):
    page_name = 'Новости игр'
    context = {
        'title': page_name,
        'page_name': page_name,
        'request': request
    }
    return templates.TemplateResponse(name='main.html', context=context)


@router_main.post('/main_create')
async def create_game(db: Annotated[Session, Depends(get_db)], create_game: CreateGame):
    db.execute(insert(Game).values(title=create_game.title,
                                   cost=create_game.cost,
                                   size=create_game.size,
                                   description=create_game.description,
                                   image=create_game.image,
                                   reviews=create_game.reviews))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router_main.delete('/delete_game')
async def delete_game(db: Annotated[Session, Depends(get_db)], game_id: int):
    game = db.scalars(select(Game).where(Game.id == game_id))
    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Game was not found')
    else:
        db.execute(delete(Game).where(Game.id == game_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}


@router_main.get('/reviews')
async def review_page(request: Request, db: Annotated[Session, Depends(get_db)]):
    page_name = 'Обзоры игр'
    games = db.scalars(select(Game)).all()
    context = {
        'page_name': page_name,
        'title': page_name,
        'games': games,
        'request': request
    }
    return templates.TemplateResponse(name='reviews.html', context=context)


@router_main.get('/game_id')
async def game_page(request: Request, db: Annotated[Session, Depends(get_db)], game_id: int):
    page_name = 'Обзор'
    game = db.scalars(select(Game).where(Game.id == game_id)).all()
    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Game was not found')
    context = {
        'page_name': page_name,
        'title': page_name,
        'game': game,
        'request': request
    }
    return templates.TemplateResponse(name='game.html', context=context)
