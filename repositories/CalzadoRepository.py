from typing import List, Optional
from models.CalzadoModel import CalzadoModel
from sqlalchemy.orm import Session, lazyload
from sqlalchemy import select
from configs.Database import (
    get_db_connection,
)

class CalzadoRepository:
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
    ) -> List[CalzadoModel]:
        query = self.db.query(CalzadoModel)

        if name:
            query = query.filter_by(nombre_producto=name)

        return query.offset(start).limit(limit).all()
    
    def get(self, calzado: CalzadoModel) -> CalzadoModel:
        return self.db.get(
            CalzadoModel,
            calzado.id,
        )

    def create(self, calzado: CalzadoModel) -> CalzadoModel:
        self.db.add(calzado)
        self.db.commit()
        self.db.refresh(calzado)
        return calzado

    def update(self, id: int, calzado: CalzadoModel) -> CalzadoModel:
        calzado.id = id
        self.db.merge(calzado)
        self.db.commit()
        return calzado

    def delete(self, calzado: CalzadoModel) -> None:
        self.db.delete(calzado)
        self.db.commit()
        self.db.flush()