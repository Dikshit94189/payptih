from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_all_users(db: Session) -> list[User]:
    statement = select(User)

    result = db.execute(statement)

    users = result.scalars().all()

    return list(users)


def get_user_by_email(
    db: Session,
    email: str
) -> User | None:
    statement = select(User).where(
        User.email == email
    )
    
    result = db.execute(statement)
    
    user = result.scalar_one_or_none()
    
    return user