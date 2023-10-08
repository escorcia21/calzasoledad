from typing import List, Optional
from models.RolesModel import Roles
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection,
)


class RolesRepository:
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
    ) -> List[Roles]:
        query = self.db.query(Roles)

        if name:
            query = query.filter_by(userType=name)

        return query.offset(start).limit(limit)
    
    def get(self, roleId: int) -> Roles:
        return self.db.get(
            Roles,
            roleId
        )

    def create(self, role: Roles) -> Roles:
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role

    def update(self, id: int, role: Roles) -> Roles:
        role.roleId = id
        self.db.merge(role)
        self.db.commit()
        return role
    
    def delete(self, roleId: int) -> None:
        self.db.query(Roles).filter_by(roleId=roleId).delete()
        self.db.commit()