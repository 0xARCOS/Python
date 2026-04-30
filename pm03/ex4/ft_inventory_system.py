import sys


def main(args: list[str]) -> None:
    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")
    for arg in args[1:]:
        parts: list[str] = arg.split(sep=":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, count_str = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(count_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    print(f"Got inventory: {inventory}")

    if not inventory:
        print("At the beginning, your inventory is usually empty")
        return

    item_list: list[str] = list[str](inventory.keys())
    print(f"Item list: {item_list}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total}")

    for item in inventory.keys():
        pct: float = round(number=inventory[item] / total * 100, ndigits=1)
        print(f"Item {item} represents {pct}%")

    most: str = item_list[0]
    for item in inventory.keys():
        if inventory[item] > inventory[most]:
            most = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")

    least: str = item_list[0]
    for item in inventory.keys():
        if inventory[item] < inventory[least]:
            least: str = item
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
    print("At the beginning of the game, your inventory is usually empty ;)")


if __name__ == "__main__":
    main(args=sys.argv)
