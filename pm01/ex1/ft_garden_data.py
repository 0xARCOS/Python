class Plant:
    """Represents a plant with its basic characteristics."""

    def __init__(self, name, height, age):
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int | float): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data():
    """Create and display a registry of garden plants
    with their height and age."""
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
