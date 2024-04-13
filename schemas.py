from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Schema for Note model
class NoteModel(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    
    model_config = ConfigDict(
        from_attributes= True
    )
    
    
# Shema for Creating a Note
class NoteCreateModel(BaseModel):
    title: str
    content: str
    
    model_config = ConfigDict(
        from_attributes= True,
        json_schema_extra={
            "example": {
                "title": "Hello World",
                "content": "This is a note"
            }
        }
    )