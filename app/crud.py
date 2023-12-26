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


def create_user(db: Session, user: UserSchema):
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        user (UserSchema): The user data.

    Returns:
        User: The created user.
    """
    _user = User(name=user.name, email=user.email, password=user.password)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def remove_user(db: Session, user_id: int):
    """
    Remove a user from the database.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to remove.

    Returns:
        User: The removed user.
    """
    _user = get_user_by_id(db=db, user_id=user_id)

    if _user is None:
        return None
    
    db.delete(_user)
    db.commit()


def update_user(db: Session, user_id: int, name: str, email: str, password: str):
    """
    Update a user in the database.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to update.
        name (str): The new name.
        email (str): The new email.
        password (str): The new password.

    Returns:
        User: The updated user.

    Examples:
        # Update user with ID 1
        update_user(db, 1, "John Doe", "john@example.com", "newpassword")
    """
    _user = get_user_by_id(db, user_id=user_id)

    if _user is None:
        return None

    _user.name = name
    _user.email = email
    _user.password = password
    db.commit()
    db.refresh(_user)
    return _user
