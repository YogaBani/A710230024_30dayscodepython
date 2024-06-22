# Define a class for the Supermarket
class Supermarket:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        print("Products in", self.name, ":")
        for product in self.products:
            print(product.name, ":", product.price)

# Define a class for the Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price} ({self.quantity} in stock)"

# Create a Supermarket instance
supermarket = Supermarket("My Supermarket", "123 Main St")

# Create some Product instances
product1 = Product("Apple", 1.99, 10)
product2 = Product("Banana", 0.99, 20)
product3 = Product("Milk", 2.49, 5)

# Add products to the supermarket
supermarket.add_product(product1)
supermarket.add_product(product2)
supermarket.add_product(product3)

# Display the products
supermarket.display_products()

# Remove a product
supermarket.remove_product(product2)

# Display the products again
supermarket.display_products()
