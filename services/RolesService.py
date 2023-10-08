from typing import List, Optional

from models.RolesModel import Roles

from repositories.RolesRepository import RolesRepository

class RolesService:
    rolesRepository: RolesRepository

    def __init__(
        self, rolesRepository: RolesRepository = RolesRepository()
    ) -> None:
        self.rolesRepository = rolesRepository

    def create(self, role_body) -> Roles:
        return self.rolesRepository.create(
            Roles(userType=role_body["userType"])
        )

    def delete(self, roleId: int) -> None:
        return self.rolesRepository.delete(roleId)


    def get(self, roleId: int) -> Roles:
        return self.rolesRepository.get(roleId)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Roles]:
        return self.rolesRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, role_body
    ) -> Roles:
        return self.rolesRepository.update(
            role_body["roleId"], Roles(userType=role_body["userType"])
        )