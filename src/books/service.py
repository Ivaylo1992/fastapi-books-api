from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from src.books.models import Book
from src.books.schemas import BookCreateModel, BookUpdateModel


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(Book.created_at)

        result = await session.exec(statement)

        return result.all()
    
    async def get_book(self, book_uuid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uuid)

        result = await session.exec(statement)

        found_book = result.first()

        return found_book if found_book else None
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()

        new_book = Book(
            **book_data_dict
        )

        session.add(new_book)

        await session.commit()

        return new_book

    async def update_book(self, book_uuid: str, update_data: BookUpdateModel, session: AsyncSession):
        book_to_update = self.get_book(book_uuid, session)

        if book_to_update:
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            await session.commit()

            return book_to_update
        
        return None
    
    async def delete_book(self, book_uuid: str, session: AsyncSession):
        book_to_delete = self.get_book(book_uuid, session)

        if book_to_delete:
            await session.delete(book_to_delete)

            await session.commit()

        else:
            return None