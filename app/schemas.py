from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class UserSchema(BaseModel):
    """
    Represents the schema for a user.
    """

    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
  
    class Config:
        orm_mode = True

class RequestUser(BaseModel):
    """
    Represents a request user.
    """
    parameters: UserSchema = Field(...)

class Response(GenericModel, Generic[T]):
    """
    Represents a generic response object.

    Attributes:
        code (str): The response code.
        status (str): The response status.
        message (str): The response message.
        result (Optional[T]): The response result, if any.
    """
    code: str
    status: str
    message: str
    result: Optional[T]
