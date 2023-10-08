from typing import List, Optional

from models.ProductionModel import Production

from repositories.ProductionRepository import ProductionRepository


class ProductionService:
    repository: ProductionRepository

    def __init__(
        self, repository: ProductionRepository = ProductionRepository()
    ) -> None:
        self.repository = repository

    def list(
        self,
        employeeId: Optional[int],
        limit: Optional[int],
        start: Optional[int],
        date: str,
    ) -> List[Production]:
        return self.repository.list(
            employeeId,
            limit,
            start,
            date,
        )

    def get(self, productionId: int) -> Production:
        return self.repository.get(productionId)

    def create(self, production_body: dict) -> Production:
        return self.repository.create(
            Production(
                employeeId=production_body["employeeId"],
                productId=production_body["productId"],
                productionDate=production_body["productionDate"],
                amount=production_body["amount"],
            )
        )

    def update(self, production_body: dict) -> Production:
        return self.repository.update(production_body["productionId"], production_body)