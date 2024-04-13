from models import Note

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select


class CRUD:
    # Get All Notes
    async def get_all(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            result = await session.execute(select(Note).order_by(Note.id))
            return result.scalars().all()

    # Create Note
    async def add(self, async_session: async_sessionmaker[AsyncSession], note: Note):
        async with async_session() as session:
            session.add(note)
            await session.commit()
            
        return note

    # Get one Note
    async def get_by_id(
        self, async_session: async_sessionmaker[AsyncSession], note_id: str
    ):
        async with async_session() as session:
            statement = select(Note).filter(Note.id == note_id)

            result = await session.execute(statement)

            return result.scalars().one()

    # Upate Note
    async def update_note(
        self, async_session: async_sessionmaker[AsyncSession], note_id, data
    ):
        async with async_session() as session:
            statement = select(Note).filter(Note.id == note_id)
            
            result = await session.execute(statement)
            
            note = result.scalars().one()

            note.title = data["title"]
            note.content = data["content"]

            await session.commit()

            return note

    # Delete Note
    async def delete(self, async_session: async_sessionmaker[AsyncSession], note: Note):
        async with async_session() as session:
            await session.delete(note)
            await session.commit()
            
        return {}
