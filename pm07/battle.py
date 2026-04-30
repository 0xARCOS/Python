from ex0 import FlameFactory, AquaFactory
from ex0.creature import CreatureFactory

def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    # Instanciamos ambos
    base = factory.create_base()
    evolved = factory.create_evolved()
    
    # Descripción y ataque de la criatura base
    print(base.describe())
    print(base.attack())
    
    # Descripción y ataque de la criatura evolucionada
    print(evolved.describe())
    print(evolved.attack())

def battle(factory1, factory2) -> None:
    print("Testing battle")
    # Obtenemos las criaturas base
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    
    # Output en líneas separadas según el subject
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    
    # Ataques finales
    print(c1.attack())
    print(c2.attack())

if __name__ == "__main__":
    # Inicializamos las fábricas
    fire_f = FlameFactory()
    aqua_f = AquaFactory()
    
    # Ejecución de las pruebas
    test_factory(fire_f)
    test_factory(aqua_f)
    battle(fire_f, aqua_f)