from fastapi import FastAPI, status

from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import List

from crud import CRUD
from db import engine
from schemas import NoteModel, NoteCreateModel
from models import Note

import uuid


app = FastAPI(
    title="Note API",
    description="A simple note API",
    version="0.0.1",
    docs_url="/",
    redoc_url="/",
    openapi_url="/openapi.json",
)

session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

db = CRUD()


# Get all Notes
@app.get("/notes", response_model=List[NoteModel], status_code=status.HTTP_200_OK)
async def get_all_notes():
    notes = await db.get_all(session)
    
    return notes


# Get note by id
@app.get("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def get_note_by_id(note_id):
    note = await db.get_by_id(session, note_id)
    return note

# Create a note
@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(note_data: NoteCreateModel):
    new_note = Note(
        id=str(uuid.uuid4()),
        title=note_data.title,
        content=note_data.content,
    )
    
    note = await db.add(session, new_note)
    return note


# Update Note
@app.patch("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def update_note(note_id: str, data: NoteCreateModel):
    note = await db.update_note(session, note_id, data={
        "title": data.title,
        "content": data.content,
    })
    return note


# Delete Note
@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id):
    note = await db.get_by_id(session, note_id)
    
    result = await db.delete(session, note)
    return result
