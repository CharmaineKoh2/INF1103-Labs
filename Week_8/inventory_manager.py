import json


class Product:

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
        print(f"ID: {self.__product_id} | "
              f"Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | "
              f"Stock: {self.__stock}")

    def to_dict(self):
        return {
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
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

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory

    except FileNotFoundError:
        with open("inventory.json", "w") as file:
            json.dump({}, file)

        return {}



def main():

    inventory = load_inventory()

    print("\n===========================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===========================")
    
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    while True:

        option = input("\nEnter option: ")

        if option == "1":
            display_all(inventory)

        elif option == "2":
            inventory = add_product(inventory)

        elif option == "3":
            inventory = update_stock(inventory)

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


main()