import math
from typing import Any, Literal


def get_player_pos() -> tuple[float, float, float]:
    found = False
    while not found:
        input_user: str = input("Enter new coordinates as floats in format 'x,y,z': ")

        try:
            values: list[str] = input_user.split(sep=",")

            if len(values) != 3:
                print("Invalid syntax: Please provide exactly three values.")
                continue

            x: float = float(values[0])
            y: float = float(values[1])
            z: float = float(values[2])

            found = True
            return (x, y, z)


        except ValueError:
            print("Error: One or more values are not valid numbers.")
            continue

        
    return (0.0, 0.0, 0.0)


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
    print(f"Got a first tuple: {coord2}")

    x2: float = coord2[0]
    y2: float = coord2[1]
    z2: float = coord2[2]

            
    except ValueError:
        print(f"Error on parameter '{_}'")
    


if __name__ == "__main__":
    main()