class ClassError(Exception):
    """
    Base error class for the entire garden system.
    """
    pass


class NameError(ClassError):
    """
    Raised when the plant name is empty.
    """
    pass


class WaterError(ClassError):
    """
    Raised when the water_level value is outside the valid limits.
    """
    pass


class SunlightError(ClassError):
    """
    Raised when the sunlight_hours value is outside the valid limits.
    """
    pass


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    This function checks if the plant parameters are valid.
    If something is wrong, it raises the corresponding error.
    """

    def check_name():
        if plant_name == "":
            raise NameError("Error: Plant name cannot be empty!")

    def check_water():
        if water_level < 1:
            raise WaterError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        if water_level > 10:
            raise WaterError(
                f"Error: Water level {water_level} is too high (max 10)"
            )

    def check_sunlight():
        if sunlight_hours < 2:
            raise SunlightError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise SunlightError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )

    check_name()
    check_water()
    check_sunlight()

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ClassError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ClassError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("lettuce", 15, 6))
    except ClassError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("carrots", 7, 0))
    except ClassError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
