from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing():
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    
    # Base
    print("base:")
    c_base = factory.create_base()
    print(c_base.describe())
    print(c_base.attack())
    print(c_base.heal())
    
    # Evolved
    print("evolved:")
    c_evolved = factory.create_evolved()
    print(c_evolved.describe())
    print(c_evolved.attack())
    print(c_evolved.heal())


def test_transform():
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()
    
    # Base
    print("base:")
    c_base = factory.create_base()
    print(c_base.describe())
    print(c_base.attack())
    print(c_base.transform())
    print(c_base.attack())
    print(c_base.revert())
    
    # Evolved
    print("evolved:")
    c_evolved = factory.create_evolved()
    print(c_evolved.describe())
    print(c_evolved.attack())
    print(c_evolved.transform())
    print(c_evolved.attack())
    print(c_evolved.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
