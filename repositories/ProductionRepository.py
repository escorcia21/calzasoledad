from typing import List, Optional
from models.ProductionModel import Production
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection,
)


class ProductionRepository:
    db: Session

    def __init__(
        self, db = next(get_db_connection())
    ) -> None:
        self.db = db

    def list(
        self,
        employeeId: Optional[int],
        limit: Optional[int],
        start: Optional[int],
        date: str,
    ) -> List[Production]:
        query = self.db.query(Production)

        if employeeId:
            query = query.filter_by(employeeId=employeeId, productionDate=date)

        return query.offset(start).limit(limit)
    
    def get(self, productionId: int) -> Production:
        return self.db.get(
            Production,
            productionId
        )

    def create(self, production: Production) -> Production:
        self.db.add(production)
        self.db.commit()
        self.db.refresh(production)
        return production
    
    def update(self, id: int, production_body: dict) -> Production:
        self.db.query(Production).filter_by(productionId=id).update(production_body)
        self.db.commit()
        return self.get(id)