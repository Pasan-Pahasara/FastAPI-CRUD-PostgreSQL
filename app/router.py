from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, Request, Response, RequestUser

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

@router.post("/create")
async def create_user(request: RequestUser, db: Session = Depends(get_db)):
    """
    Create a new user.

    Args:
        request (RequestUser): The user data to be created.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the response status, code, and message.
    """
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)

@router.delete("/delete")
async def remove_user(request: RequestUser,  db: Session = Depends(get_db)):
    """
    Remove a user from the database.

    Args:
        request (RequestUser): The user request object.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the response status, code, and message.
    """
    crud.remove_user(db, user_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)