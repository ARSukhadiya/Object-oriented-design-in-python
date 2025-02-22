class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f"Customer name={self.__name}, address={self.__address}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Customer):
            return __value.__name == self.__name
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)
        

class Product:
    def __init__(self, productid: int, product_name: str, price: float) -> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price

    @property
    def productid(self) -> int:
        return self.__productid
    
    def __str__(self) -> str:
        return f"Product productid={self.__productid}, product_name={self.__product_name}, price={self.__price}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Product):
            return __value.__productId == self.__productId
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)


class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    def total_value(self) -> int:
        return self.__price * self.__quantity

    def __str__(self) -> str:
        return f"OrderItem product={self.__product}, quantity={self.__quantity}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, OrderItem):
            return __value.__product == self.__product
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)


class Order:
    def __init__(self, orderid: int, customer: Customer) -> None:
        self.__orderid = orderid
        self.__customer = customer
        self.__items: list[OrderItem] = []

    @property
    def orderid(self) -> int:
        return self.__orderid
    
    def add_item(self, product: Product, quantity: int) -> None:
        self.__items.append(OrderItem(product, quantity))


    def __str__(self) -> str:
        return f"Order orderid={self.__orderid}, customer={self.__customer}, items={self.__items}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Order):
            return __value.__orderid == self.__orderid
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)


def main():
    p1 = Product(111, "Hammer", 25.99)
    p2 = Product(222, "Screw Driver", 15.99)
    p3 = Product(333, "Trimmer", 35.99)
    customer = Customer("Peter", "123 Mission Blvd")

    order = Order(1234, customer)
    order.add_item(p1, 10)
    order.add_item(p2, 20)
    order.add_item(p3, 15)

    print(order)

if __name__ == "__main__":
    main()
