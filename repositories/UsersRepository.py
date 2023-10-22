from typing import List, Optional
from models.UsersModel import Users
from configs.Database import Session as db


class UsersRepository:

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Users]:
        try:
            query = db.query(Users)

            if name:
                query = query.filter_by(name=name)

            return query.offset(start).limit(limit)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def get(self, userId: str) -> Users:
        try:
            return db.get(
                Users,
                userId
            )
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def create(self, user: Users) -> Users:
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def update(self, id: int, user_body: dict) -> Users:
        try:
            db.query(Users).filter_by(cc=id).update(user_body)
            db.commit()
            return self.get(id)
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def login(self, cc: str, password: str) -> Users:
        try:
            return db.query(Users).filter_by(cc=cc, password=password).first()
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
