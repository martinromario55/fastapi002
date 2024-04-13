from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
import os


load_dotenv() # If the .env file is in the same folder, you don't need to pas in any arguments

engine = create_async_engine(
    os.getenv("DATABASE_URL"),
    echo=True,
)

class Base(DeclarativeBase):
    pass