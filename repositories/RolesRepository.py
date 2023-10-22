from typing import List, Optional
from models.RolesModel import Roles
from configs.Database import Session as db


class RolesRepository:

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Roles]:
        try:
            query = db.query(Roles)

            if name:
                query = query.filter_by(userType=name)

            return query.offset(start).limit(limit)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def get(self, roleId: int) -> Roles:
        try:
            return db.get(
                Roles,
                roleId
            )
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def create(self, role: Roles) -> Roles:
        try:
            db.add(role)
            db.commit()
            db.refresh(role)
            return role
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def update(self, id: int, role: Roles) -> Roles:
        try:
            role.roleId = id
            db.merge(role)
            db.commit()
            return role
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def delete(self, roleId: int) -> None:
        try:
            db.query(Roles).filter_by(roleId=roleId).delete()
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.remove()