class GardenError(Exception):
    """ Base caase error for the entire garden system"""
    pass


class PlantError(GardenError):
    """
    Its a error class made for plants
    """
    pass


class WaterError(GardenError):
    """
    Its a error class made for water
    """
    pass


def check_plant():
    """
    This function throws PlantError
    """
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for function in [check_plant, check_water]:
        try:
            function()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
