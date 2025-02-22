class Customer:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    def __str__(self):
        return (f"Customer: name = {self.__name}, adddress = {self.__address}")
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Customer):
            return __value.__name == self.__name
        else:
            return False
    
    def __repr__(self) -> str:
        return str(self)


class Product:
    def __init__(self, productid: int, product_name: str, price: float):
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price 
    
    @property
    def productid(self):
        return self.__productid
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price: float):
        self.__price = price
        
    def __str__(self):
        return (f"Product: productid = {self.__productid}, product_name = {self.__product_name}, price = {self.__price}")
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Product):
            return __value.__productid == self.__productid
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        if quantity >= 0: 
            self.__quantity: int = quantity
        else:
            raise ValueError("Quantity Cannot be Negative!")
        
    @property
    def product(self):
        return self.__product
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self):
        return self.__quantity
    
    def __str__(self) -> str:
        return f"OrderItem : product = {str(self.__product)}, quantity = {self.__quantity}"
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, OrderItem):
            return __value.__product == self.__product
        else:
            return False
    
    def __repr__(self) -> str:
        return str(self)
        

class Order:
    def __init__(self, orderid: int, customer: Customer):
        self.__orderid = orderid
        self.__order_items: list[OrderItem] = []
        self.__customer = customer
    
    @property
    def orderid(self):
        return self.__orderid
        
    def add_item(self, order_item: OrderItem):
        self.__order_items.append(order_item)
    
    def remove_item(self, productid1: int):
        to_be_removed = None
        for item in self.__order_items:
            if item.product.productid  == productid1:
                to_be_removed = item
                break
        
        if to_be_removed == None:
            print("No Item Found")
            return 
        
        self.__order_items.remove(to_be_removed)
        
    def find_largest_item(self) -> OrderItem:
        if len(self.__order_items) == 0:
            raise ValueError("No Items present!")
        
        return max(self.__order_items,key = lambda x : x.quantity)

    def get_total(self) -> float:
        total: float = 0
        for item in self.__order_items:
            total += item.product.price * item.quantity
        
        return total
    
    def get_discount_value(self, discount_rate: float) -> float:
        return self.get_total() * discount_rate
    
    def __str__(self):
        result: str = (f"Order: orderid = {self.__orderid}, customer = {str(self.__customer)}\n")
        result += "Products are :-\n"
        for items in self.__order_items:
            result += f"product = {str(items)}\n"
        
        return result
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Order):
            return __value.__orderid == self.__orderid
        else:
            return False
        
    def __repr__(self) -> str:
        return str(self)


def main():
    customer1 = Customer("Abhishek", "123 Winema Commons")

    print("\nExample of Customer Class:")
    print(customer1)

    product1 = Product(123, "Soap", 5.0)
    product2 = Product(222, "Shampoo", 8.0)
    product3 = Product(345, "Conditioner", 11.0)

    print("\nExample of Product Class:")
    print(product1)

    orderItem1 = OrderItem(product1, 2)
    orderItem2 = OrderItem(product2, 1)
    orderItem3 = OrderItem(product3, 1)

    print("\nExample of OrderItem Class:")
    print(orderItem1)

    print("\nExample of Order Class:")
    order = Order(123, customer1)
    order.add_item(orderItem1)
    order.add_item(orderItem2)
    print("\n", order)

    print("\nAdded a new orderItem")
    order.add_item(orderItem3)
    print(order)

    print("Removed an item with productid 222")
    order.remove_item(222)
    print(order)

    print("Find the largest order item")
    print(order.find_largest_item())

    print("Find the total cost:")
    print(order.get_total())

    print("Find the total discount value with 10% discount")
    print(order.get_discount_value(0.1))


if __name__ == "__main__":
    main()
