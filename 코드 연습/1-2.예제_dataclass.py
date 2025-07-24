from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price:int
    stock:int

product = Product('이호섭',200000000,1)

print(f'{product.name}:{product.price:,}원, 재고{product.stock}개')