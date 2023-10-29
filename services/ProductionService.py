from datetime import date
from typing import List, Optional

from models.ProductionModel import Production

from repositories.ProductionRepository import ProductionRepository


class ProductionService:
    repository: ProductionRepository

    def __init__(
        self, repository: ProductionRepository = ProductionRepository()
    ) -> None:
        self.repository = repository

    def list(self) -> List[Production]:
        return self.repository.get()

    def get(self, startProductionDate: str, endProductionDate: str ,employeeId: int) -> Production:
        return self.repository.get(startProductionDate, endProductionDate, employeeId)

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