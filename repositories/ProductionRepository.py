from typing import List, Optional
from models.ProductionModel import Production
from schemas.productionSchemas import ProductionSchema
from sqlalchemy import text
from configs.Database import Session as db



class ProductionRepository:

    def list(
        self,
        employeeId: Optional[int],
        limit: Optional[int],
        start: Optional[int],
        date: str,
    ) -> List[Production]:
        try:
            query = db.query(Production)

            if employeeId:
                query = query.filter_by(employeeId=employeeId, productionDate=date)

            return query.offset(start).limit(limit)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def get(self, startProductionDate: str = None, endProductionDate: str = None,employeeId: int = None, productionId: int = None) -> Production:

        query = text("""
            SELECT 
                SUM(production.amount) AS totalAmount, 
                concat(users.name, ' ', users.lastName) AS name,
                production.productionDate,
                products.productName,
                products.unitCompensation,
                products.packagesCompensation, 
                products.price 
            FROM production 
            JOIN products ON products.productId = production.productId 
            JOIN users ON users.cc = production.employeeId 
            WHERE users.cc = :employeeId AND
            (production.productionDate BETWEEN :startProductionDate AND :endProductionDate)
            GROUP BY users.name, users.lastName, production.productionDate, products.productName, products.productId
            ORDER BY production.productionDate ASC
        """)

        if not startProductionDate or not endProductionDate or not employeeId:
            query = text("""
            SELECT 
                SUM(production.amount) AS totalAmount, 
                concat(users.name, ' ', users.lastName) AS name,
                production.productionDate,
                products.productName,
                products.unitCompensation,
                products.packagesCompensation, 
                products.price 
            FROM production 
            JOIN products ON products.productId = production.productId 
            JOIN users ON users.cc = production.employeeId
            GROUP BY users.name, users.lastName, production.productionDate, products.productName, products.productId
            ORDER BY production.productionDate ASC
        """)
            
        if productionId:
            query = text("""
            SELECT 
                SUM(production.amount) AS totalAmount, 
                concat(users.name, ' ', users.lastName) AS name,
                production.productionDate,
                products.productName,
                products.unitCompensation,
                products.packagesCompensation, 
                products.price 
            FROM production 
            JOIN products ON products.productId = production.productId 
            JOIN users ON users.cc = production.employeeId 
            WHERE production.productionId = :productionId
            GROUP BY users.name, users.lastName, production.productionDate, products.productName, products.productId
            ORDER BY production.productionDate ASC
        """)

        user_production_object = {}
        response = []
        try:
            if productionId:
                result = db.execute(query, {'productionId': productionId})
            else:
                result = db.execute(query, {
                    'employeeId': employeeId, 
                    'startProductionDate': startProductionDate,
                    'endProductionDate': endProductionDate
                })
        except:
            db.rollback()
            raise
        finally:
            db.remove()

        scheme = ProductionSchema(many=True)
        mapped_result = scheme.dump(result)

        for production in mapped_result:
            
            if production['totalAmount'] > 12:

                num_packages = production['totalAmount'] // 12
                num_units = production['totalAmount'] % 12
                
                for _ in range(num_packages):
                    package = self.packageCompensation(production)
                    response.append(package)

                if num_units > 0:
                    unit = self.unitCompensation(production, num_units)
                    response.append(unit)
            elif production['totalAmount'] == 12:
                package = self.packageCompensation(production)
                response.append(package)
            else:
                remaining = production['totalAmount']
                unit = self.unitCompensation(production, remaining)
                response.append(unit)

            
            user_production_object['production'] = response
            user_production_object['totalCompensation'] = sum([x['compensation'] for x in response])

        return  user_production_object        

    def create(self, production: Production) -> Production:
        try:
            db.add(production)
            db.flush()
            db.commit()
            db.refresh(production)
            return self.get(productionId=production.productionId)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def update(self, id: int, production_body: dict) -> Production:
        try:
            db.query(Production).filter_by(productionId=id).update(production_body)
            db.commit()
            return db.query(Production).get(id)
        except:
            db.rollback()
            raise
        finally:
            db.remove()
    
    def packageCompensation(self, production):

        packagePrice = 12 * production['price']
        packageCompensation = packagePrice * production['packagesCompensation']

        return {
            "isPackage": True,
            "compensation": packageCompensation,
            "price": packagePrice,
            "name": production['name'],
            "quantity": 12,
            "productionDate": production['productionDate'],
            "productName": production['productName'],
            "unitPrice": production['price'],
            "percentage": production['packagesCompensation']
        }

    def unitCompensation(self, production, remaining):
        remainingPrice = remaining * production['price']
        unitCompensation = remainingPrice * production['unitCompensation']
        
        return {
            "compensation": unitCompensation,
            "price": remainingPrice,
            "name": production['name'],
            "quantity": remaining,
            "productionDate": production['productionDate'],
            "productName": production['productName'],
            "unitPrice": production['price'],
            "percentage": production['packagesCompensation']
        } 