from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, Request, Response, RequestBook

import crud

router = APIRouter()

def get_db():
    """
    Returns a database session.

    Yields:
        SessionLocal: The database session.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve users from the database.

    Parameters:
    - skip (int): Number of records to skip (default: 0)
    - limit (int): Maximum number of records to retrieve (default: 100)
    - db (Session): Database session dependency

    Returns:
    - Response: HTTP response object with the fetched users
    """
    _users = crud.get_users(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)