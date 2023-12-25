from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of users from the database.

    Args:
        db (Session): The database session.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to retrieve. Defaults to 100.

    Returns:
        List[User]: A list of User objects.
    """
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve a user from the database by their ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user object if found, None otherwise.
    """
    return db.query(User).filter(User.id == user_id).first()