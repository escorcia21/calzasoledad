from typing import List, Optional

from models.UsersModel import Users

from repositories.UsersRepository import UsersRepository

class UsersService:
    usersRepository: UsersRepository

    def __init__(
        self, usersRepository: UsersRepository = UsersRepository()
    ) -> None:
        self.usersRepository = usersRepository

    def create(self, user_body) -> Users:
        return self.usersRepository.create(
            Users(cc=user_body["cc"], name=user_body["name"], lastName=user_body["lastName"], roleId=user_body["roleId"])
        )

    def get(self, userId: str) -> Users:
        return self.usersRepository.get(userId)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Users]:
        return self.usersRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, user_body
    ) -> Users:
        return self.usersRepository.update(
            user_body["cc"], user_body
        )
        