from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.schemas import BookCreateModel, BookUpdateModel


class BookService:
    async def get_all_books(self, session: AsyncSession):
        ...
    
    async def get_book(self, book_uuid: str, session: AsyncSession):
        ...
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        ...

    async def update_book(self, book_uuid: str, update_data: BookUpdateModel, session: AsyncSession):
        ...
    
    async def delete_book(self, book_uuid: str, session: AsyncSession):
        ...