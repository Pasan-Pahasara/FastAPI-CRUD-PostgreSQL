from sqlalchemy import Column, Integer, String
from config import Base


class User(Base):
    """
    Represents a user in the system.
    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
