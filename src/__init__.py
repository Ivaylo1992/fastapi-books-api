from fastapi import FastAPI
from .books.routers import book_router
from .db.main import init_db

async def life_span(app: FastAPI):
    print('The server is starting ...')
    await init_db()
    yield
    print('The server has been stopped.')


version = 'v1'

app = FastAPI(
    version=version,
    title='BooksPy',
    description='A REST API for a book review web service.',
    lifespan=life_span
)

app.include_router(book_router, prefix='/api/{version}/books', tags=['books'])