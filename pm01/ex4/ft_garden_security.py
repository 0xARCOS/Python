class SecurePlant:
    """A plant with encapsulated attributes and input validation
      via getters and setters."""

    def __init__(self, name, height, age):
        """
        Initialize a SecurePlant instance with validated height and age.

        Args:
            name (str): The name of the plant.
            height (int | float): The initial height in centimeters
            (must be >= 0).
            age (int): The initial age in days (must be >= 0).
        """
        self.__name = name
        self.__height = 0
        self.__age = 0

        print("=== Garden Security System ===")
        print(f"Plant created: {self.__name}")

        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        """Return the plant's current height in centimeters."""
        return self.__height

    def get_age(self):
        """Return the plant's current age in days."""
        return self.__age

    def get_name(self):
        """Return the plant's name."""
        return self.__name

    def set_height(self, value):
        """
        Set the plant's height after validating the input.

        Args:
            value (int | float): The new height in centimeters.
              Rejected if negative.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value):
        """
        Set the plant's age after validating the input.

        Args:
            value (int): The new age in days. Rejected if negative.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = value
            print(f"Age updated: {value}cm [OK]\n")

    def status(self):
        """Print the plant's current name, height, and age."""
        print(f"Current plant: {self.__name} "
              f"({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    p1 = SecurePlant("Rose", 25, 30)
    p1.set_age(-5)
    p1.status()
