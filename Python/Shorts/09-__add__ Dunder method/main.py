class ShoppingCartItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, ShoppingCartItem):
            # Combine the prices and create a new item
            new_name = f"{self.name} and {other.name}"
            new_price = self.price + other.price
            return ShoppingCartItem(new_name, new_price)
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))


# Creating two instances of ShoppingCartItem
item1 = ShoppingCartItem("Apples", 2.50)
item2 = ShoppingCartItem("Bananas", 1.75)

# Using the addition operator (+) calls __add__
combined_item = item1 + item2

# Displaying the result
print(combined_item.price)
