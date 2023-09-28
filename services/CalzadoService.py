from typing import List, Optional

from models.CalzadoModel import CalzadoModel

from repositories.CalzadoRepository import CalzadoRepository
from schemas.Calzado import CalzadoSchema


class CalzadoService:
    calzadoRepository: CalzadoRepository

    def __init__(
        self, calzadoRepository: CalzadoRepository = CalzadoRepository()
    ) -> None:
        self.calzadoRepository = calzadoRepository

    def create(self, author_body: CalzadoSchema) -> CalzadoModel:
        return self.calzadoRepository.create(
            CalzadoModel(name=author_body.name)
        )

    def delete(self, author_id: int) -> None:
        return self.calzadoRepository.delete(
            CalzadoModel(id=author_id)
        )

    def get(self, author_id: int) -> CalzadoModel:
        return self.calzadoRepository.get(
            CalzadoModel(id=author_id)
        )

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[CalzadoModel]:
        return self.calzadoRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, author_id: int, author_body: CalzadoSchema
    ) -> CalzadoModel:
        return self.calzadoRepository.update(
            author_id, CalzadoModel(name=author_body.name)
        )