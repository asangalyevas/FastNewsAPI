"""
Module for database connections
"""
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .environs import *

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(url=DATABASE_URL)
session = async_sessionmaker(bind=engine, expire_on_commit=True)

class Base(DeclarativeBase):
    """
    Meta class for sqlalchemy ORM models
    """