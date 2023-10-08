from typing import List, Optional

from models.RolesModel import Roles

from repositories.RolesRepository import RolesRepository
from schemas.RolesSchemas import CreateRoleSchema, UpdateRoleSchema


class RolesService:
    rolesRepository: RolesRepository

    def __init__(
        self, rolesRepository: RolesRepository = RolesRepository()
    ) -> None:
        self.rolesRepository = rolesRepository

    def create(self, role_body: CreateRoleSchema) -> Roles:
        return self.rolesRepository.create(
            Roles(userType=role_body.userType)
        )

    def delete(self, roleId: int) -> None:
        return self.rolesRepository.delete(
            Roles(roleId=roleId)
        )

    def get(self, roleId: int) -> Roles:
        return self.rolesRepository.get(
            Roles(roleId=roleId)
        )

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
        self, roleId: int, role_body: UpdateRoleSchema
    ) -> Roles:
        return self.rolesRepository.update(
            roleId, Roles(userType=role_body.userType)
        )