from datetime import datetime
from sqlalchemy import DateTime, Integer, Numeric, String

from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    
    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    age:Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    
    phone:Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )
    
    salary:Mapped[float] = mapped_column(
        Numeric(12,2),
        nullable=False
    )
    
    role:Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    
    email:Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True
    )
    
    password_hash:Mapped[str] = mapped_column(
        String(25),
        nullable=False
    )
    
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )