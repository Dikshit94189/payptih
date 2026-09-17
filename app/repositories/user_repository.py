from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_all_users(db: Session) -> list[User]:
    statement = select(User)

    result = db.execute(statement)

    users = result.scalars().all()

    return list(users)