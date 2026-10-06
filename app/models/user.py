from enum import unique

from sqlalchemy import String
from sqlalchemy.orm import Mapped,MappedColumn
from sqlalchemy.testing.schema import mapped_column

from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
