from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pages.router import *
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.include_router(router_main)
app.mount('/static', StaticFiles(directory='static'), 'static')


