import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_user: str = input("Enter new coordinates as \
             floats in format 'x,y,z': ")
        values: list[str] = input_user.split(sep=",")

        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(values[0])
            y: float = float(values[1])
            z: float = float(values[2])
            return (x, y, z)

        except ValueError:
            for value in values:
                try:
                    float(value)
                except ValueError as e:
                    print(f"Error on parameter '{value.strip()}': {e}")
                    break


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coord1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {coord1}")

    x1: float = coord1[0]
    y1: float = coord1[1]
    z1: float = coord1[2]

    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_center: float = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {dist_center:.4f}")

    print("Get a second set of coordinates")
    coord2: tuple[float, float, float] = get_player_pos()

    x2: float = coord2[0]
    y2: float = coord2[1]
    z2: float = coord2[2]

    dist: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {dist:.4f}")


if __name__ == "__main__":
    main()
