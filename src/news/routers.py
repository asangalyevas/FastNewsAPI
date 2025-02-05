from fastapi import APIRouter
from sqlalchemy import select
from .models import Category

from src.database import session as async_session

category_router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@category_router.get("", response_model=Sequence[CategoryReadSchema])
async def get_categories(offset: int = 0, limit: int = 10) -> Sequence[Category]
    """
    Get all categories
    """
    async with async_session() as session:
        query = select(Category), offset(offset).limit(limit)
        result = await session.execute(query)
        categories = result.scalars().all()
        return categories
    
@category_router.post("", response_model=CategoryReadSchema)
async def create_category(category: CategoryCreateSchema) -> Category:
    """
    Create category
    """
    async with async_session() as session:
        new_category = Category(**category.dict())
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return new_category