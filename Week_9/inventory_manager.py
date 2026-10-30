import json
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        return (f"ID: {self.__product_id} | "
                f"Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | "
                f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        base_info = super().display_information()
        print(f"{base_info} | Type: Physical | Weight: {self.__weight}kg")
        print(f"Fulfilment: {self.get_fulfilment_info()}")
        print(f"Estimated Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def get_fulfilment_info(self):
        return "This product requires physical shipping via courier."

    def calculate_shipping_cost(self):
        return 5.0 + (self.__weight * 2.0)

    def to_dict(self):
        return {
            "type": "physical",
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.__weight
        }

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        base_info = super().display_information()
        print(f"{base_info} | Type: Digital | Download Size: {self.__download_size}MB")
        print(f"Fulfilment: {self.get_fulfilment_info()}")

    def get_fulfilment_info(self):
        return "This product is delivered digitally via a secure download link."

    def to_dict(self):
        return {
            "type": "digital",
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.__download_size
        }

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("\nProduct ID already exists.")
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("------------------------------------------------")
        if len(self.__products) == 0:
            print("No products available.")
        else:
            for product in self.__products:
                product.display_information()
                print("------------------------------------------------")

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)
        if product is None:
            return False
        product.update_stock(quantity)
        return True

    def get_products(self):
        return self.__products

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    
    if inventory.search_product(product_id) is not None:
        print("\nProduct ID already exists.")
        return

    name = input("Product Name: ")

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("\nInvalid price or stock quantity.")
        return

    if price < 0 or stock < 0:
        print("\nPrice and stock cannot be negative.")
        return

    print("\nSelect Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")
    choice = input("Enter option (1-2): ")

    if choice == "1":
        try:
            weight = float(input("Weight (kg): "))
            if weight < 0:
                print("Weight cannot be negative.")
                return
        except ValueError:
            print("Invalid weight.")
            return
        product = PhysicalProduct(product_id, name, price, stock, weight)

    elif choice == "2":
        try:
            download_size = float(input("Download Size (MB): "))
            if download_size < 0:
                print("Download size cannot be negative.")
                return
        except ValueError:
            print("Invalid download size.")
            return
        product = DigitalProduct(product_id, name, price, stock, download_size)

    else:
        print("\nInvalid product type choice.")
        return

    if inventory.add_product(product):
        print("\nProduct added successfully!")

def display_all(inventory):
    inventory.display_all()

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found:")
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")

        stock_input = input("\nNew Stock Quantity: ")
        if not stock_input.isdigit():
            print("Invalid stock quantity.")
            return

        quantity = int(stock_input)
        if inventory.update_stock(product_id, quantity):
            print("\nStock updated successfully!")
    else:
        print("\nProduct not found.")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found")
        print("------------------------------------------------")
        product.display_information()
        print("------------------------------------------------")
    else:
        print("\nProduct not found.")

def load_inventory():
    inventory = Inventory()
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for product_id, product_data in data.items():
            p_type = product_data.get("type")
            name = product_data["name"]
            price = product_data["price"]
            stock = product_data["stock"]

            if p_type == "physical":
                product = PhysicalProduct(product_id, name, price, stock, product_data["weight"])
            elif p_type == "digital":
                product = DigitalProduct(product_id, name, price, stock, product_data["download_size"])
            else:
                continue

            inventory.add_product(product)

    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")

    return inventory

def save_inventory(inventory):
    data = {}
    for product in inventory.get_products():
        data[product.get_product_id()] = product.to_dict()

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nSaving inventory...")
    print("Inventory saved successfully to inventory.json.")

def main():
    inventory = load_inventory()

    print("\n===========================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===========================")

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        option = input("\nEnter option: ")

        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("\nInvalid option. Please enter 1-6.")

if __name__ == "__main__":
    main()