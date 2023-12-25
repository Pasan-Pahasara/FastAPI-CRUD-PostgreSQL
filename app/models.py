from sqlalchemy import Column, Integer, String
from app.config import Base

class User(Base):
    """
    Represents a user in the system.
    """

    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"