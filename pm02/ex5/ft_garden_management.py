class GardenError(Exception):
    """Base error class for the entire garden system."""
    pass


class InvalidPlantError(GardenError):
    """Raised when plant name or input data is incorrect."""
    pass


class PlantNotFoundError(GardenError):
    """Raised when attempting to acton a non-existent plant."""
    pass


class WaterLevelError(GardenError):
    """Raised when a plant's water level exceeds the allowed maximum."""
    pass


class Plant:
    """Represents a plant with water and sun health attributes."""

    MAX_WATER = 10

    def __init__(self, name, water=0, sun=0):
        """Initialize a plant with a name and optional water/sun levels."""
        self.name = name
        self.water = water
        self.sun = sun

    def check_health(self) -> str:
        """Return a health summary string or
        raise WaterLevelError if overwatered."""
        if self.water > self.MAX_WATER:
            raise WaterLevelError(
                f"Water level {self.water} is too high (max {self.MAX_WATER})"
            )
        return f"{self.name}: healthy (water: {self.water}, sun: {self.sun})"


class GardenManager:
    """Manages a collection of plants with
    add, water, and health-check operations."""

    def __init__(self):
        """Initialize the garden with an empty plant list."""
        self.plants = []

    def add_plant(self, name, water=0, sun=0) -> None:
        """Add a plant to the garden.
        Raises InvalidPlantError if name is empty."""
        if name == "":
            raise InvalidPlantError("Plant name cannot be empty!")
        self.plants.append(Plant(name, water, sun))
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plants in the garden.
        Always closes the watering system on exit."""
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Check and print the health status of every plant in the garden."""
        print("Checking plant health...")
        for plant in self.plants:
            try:
                print(plant.check_health())
            except WaterLevelError as e:
                print(f"Error checking {plant.name}: {e}")


def test_garden_management() -> None:
    """Run a full integration test of the GardenManager system."""
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato", water=5, sun=8)
    garden.add_plant("lettuce", water=15, sun=6)
    try:
        garden.add_plant("")
    except InvalidPlantError as e:
        print(f"Error adding plant: {e}")

    print()
    garden.water_plants()

    print()
    garden.check_health()

    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
