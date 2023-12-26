from fastapi import APIRouter, HTTPException
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestUser

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
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users).model_dump()


@router.get("/{id}")
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by their ID.

    Parameters:
    - id (int): The ID of the user to retrieve.
    - db (Session): The database session.

    Returns:
    - dict: A dictionary containing the user information.
    """
    _user = crud.get_user_by_id(db, user_id=id)

    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return Response(status="Ok", code="200", message="Success fetch data", result=_user).model_dump()


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
    _user = crud.create_user(db, user=request.parameters)
    return Response(status="Ok", code="200", message="User created successfully", result=_user).model_dump()


@router.delete("/{id}")
async def remove_user(id: int, db: Session = Depends(get_db)):
    """
    Remove a user from the database.

    Args:
        request (RequestUser): The user request object.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        dict: A dictionary containing the response status, code, and message.
    """
    _user = crud.remove_user(db, user_id=id)

    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return Response(status="Ok", code="200", message="Success delete data", result=_user).model_dump()


@router.patch("/update")
async def update_user(request: RequestUser, db: Session = Depends(get_db)):
    """
    Update user data in the database.

    Args:
        request (RequestUser): The request object containing user data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        Response: The response object containing the updated user data.
    """
    _user = crud.update_user(db, user_id=request.parameters.id, name=request.parameters.name,
                             email=request.parameters.email, password=request.parameters.password)

    if _user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return Response(status="Ok", code="200", message="Success update data", result=_user).model_dump()
