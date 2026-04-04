import sys


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]


def main(args: list[str]) -> None:
    if len(args) < 2:
        msg = "Usage: python3 ft_inventory_system.py "
        msg += "item1:qty1 item2:qty2 ..."
        print(msg)
        sys.exit(1)

    inventory = {}
    for arg in args[1:]:
        try:
            name, count_str = arg.split(":")
            cantidad = int(count_str)
            inventory[name] = cantidad
        except ValueError:
            continue

    total_items = sum(inventory.values())
    unique_types = len(inventory.keys())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    sorted_inv = list(inventory.items())
    bubble_sort(sorted_inv)

    for name, value in sorted_inv:
        porcentage = (value / total_items) * 100
        unit_label = "unit" if value == 1 else "units"
        print(f"{name}: {value} {unit_label} ({porcentage:.1f}%)")

    max_val = max(inventory.values())
    most_abundant_name = 0
    for item, value in inventory.items():
        if value == max_val:
            most_abundant_name = item

    min_val = min(inventory.values())
    least_abundant_name = 0
    for item, value in inventory.items():
        if value == min_val:
            least_abundant_name = item

    print("\n=== Item Statistics ===")
    print(f"Most abundant: {most_abundant_name} ({max_val} units)")
    print(f"Least abundant: {least_abundant_name} ({min_val} unit)")

    categories = {
        "Moderate": {},
        "Scarce": {}
    }

    for name, value in inventory.items():
        if value >= 5:
            categories["Moderate"][name] = value
        else:
            categories["Scarce"][name] = value

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    restock_list = []
    for name, value in inventory.items():
        if value <= 1:
            restock_list.append(name)

    print("\n=== Management Suggestion ===")
    restock_str = ""
    for i in range(len(restock_list)):
        if i > 0:
            restock_str += ", "
        restock_str += restock_list[i]
    print(f"Restock needed: {restock_str}")

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ""
    for key in inventory.keys():
        if keys_str:  # Si no está vacío, añade coma
            keys_str += ", "
        keys_str += key
    print(f"Dictionary keys: {keys_str}")

    values_str = ""
    for val in inventory.values():
        if values_str:
            values_str += ", "
        values_str += str(val)
    print(f"Dictionary values: {values_str}")

    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main(sys.argv)
