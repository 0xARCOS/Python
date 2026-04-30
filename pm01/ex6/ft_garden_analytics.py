class Plant:
    """Base class representing a generic plant with a name and height."""

    def __init__(self, name, height):
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int | float): The initial height in centimeters.
        """
        self.name = name
        self.height = height

    def grow(self, amount=1):
        """
        Increase the plant's height and print the growth event.

        Args:
            amount (int | float): Centimeters to add. Defaults to 1.
        """
        self.height += amount
        print(self.name + " grew " + str(amount) + "cm")

    def describe(self):
        """Return a string with the plant's name and current height."""
        return self.name + ": " + str(self.height) + "cm"


class FloweringPlant(Plant):
    """A plant that produces colored flowers. Inherits from Plant."""

    def __init__(self, name, height, color):
        """
        Initialize a FloweringPlant instance.

        Args:
            name (str): The name of the plant.
            height (int | float): The initial height in centimeters.
            color (str): The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def describe(self):
        """Return name, height, flower color, and blooming status."""
        if self.blooming is True:
            status = "blooming"
        else:
            status = "dormant"
        return (self.name + ": " + str(self.height) + "cm, "
                + self.color + " flowers (" + status + ")")


class PrizeFlower(FloweringPlant):
    """A flowering plant eligible for competitions.

    Inherits from FloweringPlant.
    """

    def __init__(self, name, height, color, prize_points):
        """
        Initialize a PrizeFlower instance.

        Args:
            name (str): The name of the flower.
            height (int | float): The initial height in centimeters.
            color (str): The color of the flowers.
            prize_points (int): Competition points awarded for this flower.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self):
        """Return the base flowering plant description plus prize points."""
        base_info = super().describe()
        return base_info + ", Prize points: " + str(self.prize_points)


class GardenManager:
    """Manages a collection of plants and tracks garden-wide statistics."""

    class GardenStats:
        """Tracks cumulative addition and growth events for a single garden."""

        def __init__(self):
            """Initialize counters for plants added and total growth."""
            self.plants_added = 0
            self.total_growth = 0

        def record_addition(self):
            """Increment the count of plants added to the garden."""
            self.plants_added += 1

        def record_growth(self, amount):
            """
            Accumulate growth into the total growth counter.

            Args:
                amount (int | float): Centimeters of growth to record.
            """
            self.total_growth += amount

        def count_types(self, plants):
            """
            Count plants by exact type across the three supported categories.

            Args:
                plants (list[Plant]): The list of plants to classify.

            Returns:
                tuple[int, int, int]: Counts of regular, flowering, prize.
            """
            regular = 0
            flowering = 0
            prize = 0
            for _ in plants:
                if type(_) is Plant:
                    regular += 1
                elif type(_) is FloweringPlant:
                    flowering += 1
                elif type(_) is PrizeFlower:
                    prize += 1
            return regular, flowering, prize

        def report(self, plants):
            """
            Print a summary of additions, growth, and plant-type breakdown.

            Args:
                plants (list[Plant]): The current list of plants in the garden.
            """
            regular, flowering, prize = self.count_types(plants)
            print("\nPlants added: " + str(self.plants_added)
                  + ", Total growth: " + str(self.total_growth) + "cm")
            print("Plant types: " + str(regular) + " regular, "
                  + str(flowering) + " flowering, "
                  + str(prize) + " prize flowers\n")

    total_gardens = 0

    def __init__(self, manager_name):
        """
        Initialize a GardenManager and increment the global garden counter.

        Args:
            manager_name (str): The name of the manager who owns this garden.
        """
        self.manager_name = manager_name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        """
        Add a plant to the garden and record the addition in stats.

        Args:
            plant (Plant): The plant instance to add.
        """
        self.plants.append(plant)
        self.stats.record_addition()
        print("Added " + plant.name + " to "
              + self.manager_name + "'s garden")

    def grow_all(self, amount=1):
        """
        Apply growth to every plant in the garden and update stats.

        Args:
            amount (int | float): Centimeters of growth per plant.
            Defaults to 1.
        """
        print("\n" + self.manager_name + " is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.stats.record_growth(amount)

    def garden_score(self):
        """
        Calculate the garden's total score based on height and prize points.

        Returns:
            int | float: Sum of all plant heights plus prize points.
        """
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    def print_report(self):
        """Print a full garden report: plant descriptions and overall stats."""
        print("\n=== " + self.manager_name + "'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("  - " + plant.describe())
        self.stats.report(self.plants)

    @classmethod
    def create_garden_network(cls, names):
        """
        Create multiple GardenManager instances from a list of manager names.

        Args:
            names (list[str]): Names for each garden manager to create.

        Returns:
            list[GardenManager]: A list of newly created GardenManager
            instances.
        """
        gardens = []
        for name in names:
            gardens.append(cls(name))
        return gardens

    @staticmethod
    def validate_height(height):
        """
        Check that a given height value is non-negative.

        Args:
            height (int | float): The height value to validate.

        Returns:
            bool: True if height is >= 0, False otherwise.
        """
        if height >= 0:
            return True
        return False


def main():
    """
    Run a demo of the garden management system.

    Creates two managers, adds different plant types to Alice's garden,
    grows all plants, and prints reports and final scores.
    """
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()
    alice.print_report()

    print("Height validation test:", GardenManager.validate_height(10))

    bob.add_plant(Plant("Cactus", 40))
    bob.add_plant(FloweringPlant("Lavender", 30, "purple"))
    bob.grow_all()

    print("Garden scores - Alice: " + str(alice.garden_score())
          + ", Bob: " + str(bob.garden_score()))
    print("Total gardens managed:", GardenManager.total_gardens)


if __name__ == "__main__":
    main()
