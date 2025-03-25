from fastapi import FastAPI
from .routers import book_router

version = 'v1'

app = FastAPI(
    version=version,
    title='BooksPy',
    description='A REST API for a book review web service.'
)



app.include_router(book_router, prefix='api/{version}/books', tags=['books'])

