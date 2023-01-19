from typing import Optional
from sqlmodel import SQLModel, Field


class PasswordsBase(SQLModel):

    # Base model for password
    service_name: str = Field(default=None, index=True)
    password: str


class Passwords(PasswordsBase, table=True):

    # Main table model for passwords
    id: Optional[int] = Field(default=None, primary_key=True)


class PasswordRead(PasswordsBase):
    service_name: str
    password: str


class PasswordCreateUpdate(PasswordsBase):
    id: Optional[int] = None
    password: Optional[str] = None
    service_name: Optional[str] = None
