def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    inventory[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("\nProduct added successfully!")

    return inventory


def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product_id, product in inventory.items():
        print(
            f"ID: {product_id} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )
    print("------------------------------------------------")


def main():

    inventory = {}

    inventory = add_product(inventory)
    inventory = add_product(inventory)
    inventory = add_product(inventory)

    display_all(inventory)

main()