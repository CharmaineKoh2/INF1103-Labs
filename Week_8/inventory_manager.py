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

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory

    except FileNotFoundError:
        with open("inventory.json", "w") as file:
            json.dump({}, file)

        return {}

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("\nSaving inventory...")
    print("Inventory saved successfully to invetory.json.")

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