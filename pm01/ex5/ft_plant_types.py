class Plant:
    """Base class representing a generic plant with common attributes."""

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


class Flower(Plant):
    """A flowering plant with a distinctive color. Inherits from Plant."""

    def __init__(self, name, height, age, color):
        """
        Initialize a Flower instance.

        Args:
            name (str): The name of the flower.
            height (int | float): The height in centimeters.
            age (int): The age in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a message indicating that the flower is blooming."""
        print(self.name + " is blooming beautifully!")


class Tree(Plant):
    """A tree with a measurable trunk that can cast shade.
    Inherits from Plant."""

    def __init__(self, name, height, age, trunk_diameter):
        """
        Initialize a Tree instance.

        Args:
            name (str): The name of the tree.
            height (int | float): The height in centimeters.
            age (int): The age in days.
            trunk_diameter (int | float): The diameter of the
            trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculate and print the shade area provided by the
        tree in square meters."""
        shade_area = self.trunk_diameter * self.height // 32
        print(self.name + " provides "
              + str(shade_area) + " square meters of shade")


class Vegetable(Plant):
    """An edible plant with a harvest season and a known nutritional
    value. Inherits from Plant."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initialize a Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            height (int | float): The height in centimeters.
            age (int): The age in days.
            harvest_season (str): The season in which the vegetable
            is harvested.
            nutritional_value (str): The primary nutrient the
              vegetable is rich in.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self):
        """Print the main nutritional contribution of the vegetable."""
        print(self.name + " is rich in " + self.nutritional_value)


def main():
    """Instantiate and display info for several flowers,
      trees, and vegetables."""
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 20, "yellow")
    print(rose.name + " (Flower): " + str(rose.height) + "cm, "
          + str(rose.age) + " days, " + rose.color + " color")
    rose.bloom()
    print(tulip.name + " (Flower): " + str(tulip.height) + "cm, "
          + str(tulip.age) + " days, " + tulip.color + " color")
    tulip.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 900, 30)
    print(oak.name + " (Tree): " + str(oak.height) + "cm, "
          + str(oak.age) + " days, "
          + str(oak.trunk_diameter) + "cm diameter")
    oak.produce_shade()
    print(pine.name + " (Tree): " + str(pine.height) + "cm, "
          + str(pine.age) + " days, "
          + str(pine.trunk_diameter) + "cm diameter")
    pine.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 60, "autumn", "beta-carotene")
    print(tomato.name + " (Vegetable): " + str(tomato.height) + "cm, "
          + str(tomato.age) + " days, " + tomato.harvest_season + " harvest")
    tomato.describe_nutrition()
    print(carrot.name + " (Vegetable): " + str(carrot.height) + "cm, "
          + str(carrot.age) + " days, " + carrot.harvest_season + " harvest")
    carrot.describe_nutrition()


if __name__ == "__main__":
    main()
