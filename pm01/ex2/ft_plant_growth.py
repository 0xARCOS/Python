class Plant:
    """Represents a plant that can grow over time."""

    def __init__(self, name, height, age):
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int | float): The initial height of the
             plant in centimeters.
            age (int): The initial age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm):
        """
        Increase the plant's height.

        Args:
            cm (int | float): The number of centimeters to add
              to the current height.
        """
        self.height += cm

    def add_age(self, days):
        """
        Advance the plant's age.

        Args:
            days (int): The number of days to add to the current age.
        """
        self.age += days


def get_info():
    """Simulate one week of growth for a Rose and print its
      state before and after."""
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    week_growth = 6
    rose.grow(week_growth)
    rose.add_age(6)

    print("=== Day 7 ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"Growth this week: +{week_growth}cm")


if __name__ == "__main__":
    get_info()
