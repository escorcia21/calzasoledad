from typing import List, Optional
from models.ProductsModel import Products
from configs.Database import Session as db


class ProductsRepository:

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Products]:
        try:
            query = db.query(Products)

            if name:
                query = query.filter_by(productName=name)

            return query.offset(start).limit(limit)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def get(self, productId: int) -> Products:
        try:
            return db.get(
                Products,
                productId
            )
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def create(self, product: Products) -> Products:
        try:
            db.add(product)
            db.commit()
            db.refresh(product)
            return product
        except:
            db.rollback()
            raise
        finally:
            db.remove()

    def update(self, id: int, product_body: dict) -> Products:
        try:
            db.query(Products).filter_by(productId=id).update(product_body)
            db.commit()
            return self.get(id)
        except:
            db.rollback()
            raise
        finally:
            db.remove()