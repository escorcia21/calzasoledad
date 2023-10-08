from typing import List, Optional

from models.ProductsModel import Products

from repositories.ProductsRepository import ProductsRepository

class ProductsService:
    productsRepository: ProductsRepository

    def __init__(
        self, productsRepository: ProductsRepository = ProductsRepository()
    ) -> None:
        self.productsRepository = productsRepository

    def create(self, product_body) -> Products:
        return self.productsRepository.create(
            Products(
                productName=product_body["productName"],
                price=product_body["price"],
                unitCompensation=product_body["unitCompensation"],
                packagesCompensation=product_body["packagesCompensation"],
                productRoleId=product_body["productRoleId"]
            )
        )

    def get(self, productId: int) -> Products:
        return self.productsRepository.get(productId)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Products]:
        return self.productsRepository.list(
            name, pageSize, startIndex
        )

    def update(
        self, product_body
    ) -> Products:
        return self.productsRepository.update(product_body["productId"], product_body)