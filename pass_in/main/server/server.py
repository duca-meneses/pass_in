from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pass_in.main.routes.event_routes import event_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)


@app.get('/')
def read_root():
    return {'message': 'FastAPI está ligado.'}


app.include_router(event_router)