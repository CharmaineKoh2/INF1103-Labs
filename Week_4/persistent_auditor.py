def get_valid_input():
    item = input("\nEnter Product Name: ")

    if item.lower() == "quit":
        return "quit"

    quantity_input = input("Enter Quantity: ")

    if not quantity_input.isdigit():
        print("Invalid quantity. Please enter a number.")
        return None

    quantity = int(quantity_input)

    if quantity < 0:
        print("Quantity cannot be negative. Please enter a valid number.")
        return None

    return item, quantity

def add_order(history, item, quantity):
    order_id = 1001 + len(history)
    history.append([order_id, item, quantity])
    return history

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return []

        history = eval(lines[0])

        return history
    
    except FileNotFoundError:
        return []
    
def save_inventory(history):
    with open("inventory.txt", "w") as file:
        file.write(str(history))


def main():
    history = load_inventory()
    errors = 0

    print("Current Orders:\n")

    for order in history:
        print(f"{order[0]}, {order[1]}, {order[2]}")

    while True:
        result = get_valid_input()

        if result == "quit":
            save_inventory(history)
            break

        elif result is None:
            errors += 1
            continue

        item, quantity = result

        history = add_order(history, item, quantity)

        print("\nNew Order Added:")
        print(f"{history[-1][0]}, {history[-1][1]}, {history[-1][2]}")

        save_inventory(history)

        print("\nOrder successfully saved to inventory.txt")

main()