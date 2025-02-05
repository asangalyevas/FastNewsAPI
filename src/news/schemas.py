"""
Pydantic
"""

from datetime import datetime

from .models import Category

from pydantic import BaseModel


class CategoryReadSchema(BaseModel):
    """
    """
    id: int
    name: str
    created: datetime

    class Config:
        orm_mode = True

class CategoryCreateSchemas(BaseModel):
    name: str