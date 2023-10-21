from typing import List, Optional
from models.ProductsModel import Products
from sqlalchemy.orm import Session
from configs.Database import (
    get_db_connection,
)


class ProductsRepository:
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
    ) -> List[Products]:
        query = self.db.query(Products)

        if name:
            query = query.filter_by(productName=name)

        return query.offset(start).limit(limit).all()
    
    def get(self, productId: int) -> Products:
        return self.db.get(
            Products,
            productId
        )

    def create(self, product: Products) -> Products:
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except:
            self.db.rollback()
            raise

    def update(self, id: int, product_body: dict) -> Products:
        try:
            self.db.query(Products).filter_by(productId=id).update(product_body)
            self.db.commit()
            return self.get(id)
        except:
            self.db.rollback()
            raise