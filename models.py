from db import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, func

from datetime import datetime, timezone

"""
class Note:
    id str
    title str
    contentd str
    created_at datetime
"""


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=func.now()
    )

    def __repr__(self) -> str:
        return f"<Note {self.title} created at {self.created_at}>"
