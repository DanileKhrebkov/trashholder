import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod
from decorator import decorator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', encoding='UTF-8')

@dataclass
class Product:
    id: int
    name:str
    price:float
    quantity:int

    def __post_init__(self) -> None:
        logging.info(f'Был создан продукт {self.name}, его id: {self.id}')

class ProductOperation(ABC):
    @abstractmethod
    def update_price(self, new_price:float,) -> None:
        pass

    @abstractmethod
    def apply_discount(self, discount:float,) -> None:
        pass


class ProductWithDiscount(Product,ProductOperation):
    def update_price(self, new_price:float)->None:
        logging.info(f'Product:{self.name}, Old price:{self.price}, New price:{new_price}')
        self.price = new_price

    def apply_discount(self, discount:float)->None:
        discount_price = self.price * (discount/100)
        logging.info(f'Product: {self.name}, Discount: {discount}, New price: {discount_price}')


@decorator
def log_function(func, *args, **kwargs):
    logging.info(f'Вызов функции {func.__name__} с аргументами {args} и {kwargs}')
    result = func(*args, **kwargs)
    logging.info(f'Функция {func.__name__} вернула результат  {result}')
    return result


@log_function
def create_product(id:int, name:str, price:float, quantity: int) ->ProductWithDiscount:
    return ProductWithDiscount(id,name,price,quantity)

@log_function
def upgrade_product_price(product: ProductWithDiscount, new_price:float):
    product.update_price(new_price)

obj1 = create_product(1, 'notebook', 29999.99, 34)
upgrade_product_price(obj1, 59999.99)
obj1.apply_discount(19)