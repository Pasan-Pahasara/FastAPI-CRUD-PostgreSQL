from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/python_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

"""
This module provides the configuration settings for the application.

- `DATABASE_URL`: The URL of the PostgreSQL database.
- `engine`: The SQLAlchemy engine object for connecting to the database.
- `SessionLocal`: The sessionmaker object for creating database sessions.
- `Base`: The declarative base class for defining database models.
"""
