class Plant:
    """Represents a plant with a name, height, and age."""

    def __init__(self, name, height, age):
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        """Return a string representation of the plant."""
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main():
    """Create a garden of plants and display their information."""
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    garden = []
    count = 0

    for name, height, age in plant_data:
        new_plant = Plant(name, height, age)
        garden.append(new_plant)
        count += 1

    print("=== Plant Factory Output ===")

    for plant in garden:
        print(plant)

    print("Total plants created:", count)


if __name__ == "__main__":
    main()
