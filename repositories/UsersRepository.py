from typing import List, Optional
from models.UsersModel import Users
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection,
)


class UsersRepository:
    db: Session

    def __init__(
        self, db = next(get_db_connection())
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Users]:
        query = self.db.query(Users)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit)
    
    def get(self, userId: str) -> Users:
        return self.db.get(
            Users,
            userId
        )

    def create(self, user: Users) -> Users:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except:
            self.db.rollback()
            raise

    def update(self, id: int, user_body: dict) -> Users:
        try:
            self.db.query(Users).filter_by(cc=id).update(user_body)
            self.db.commit()
            return self.get(id)
        except:
            self.db.rollback()
            raise
    
