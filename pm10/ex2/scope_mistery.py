from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    """
    Crea un cierre que cuenta las veces que se ha
    llamado a la función.
    """
    # Esta variable vive en el ámbito de la función externa (factory)
    count = 0

    def counter() -> int:
        # Usamos nonlocal para indicar que queremos modificar
        # la variable 'count' del ámbito superior inmediato
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Retorna una función que acumula poder sobre una base inicial.
    Cada llamada a suma el nuevo poder al total persistente."""
    # El poder inicial se guarda en el ámbito de la función externa
    total_power = initial_power

    def accumulator(added_power: int) -> int:
        # Usamos el nonlocal para modificar el total caputurado en el closure
        nonlocal total_power
        total_power += added_power
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Retorna una función que aplica el encantamiento específico a un objeto
    """
    # Aquí la función interna "captura" enchantment_type del ámbito superior
    def apply_enchantment(item_name: str) -> str:
        # Retorna el formato obligatorio: "enchantment_type item_name"
        return f"{enchantment_type} {item_name}"

    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    """
    Crea un sistema de gestión de memoria privada.
    Retorna un diccionario con las funciones 'store' y 'recall'.
    """
    # Este es nuestro almacenamiento privado (el "cuaderno")
    # Vive en el cierre y no es accesible fuera de la función
    vault_storage = {}

    def store(key: str, value: Any) -> None:
        """
        Guarda un valor asociado a una clave en la bóveda.
        """
        # Al modificar el contenido de un objeto mutable (dict),
        # no necesitamos nonlocal, pero la variable sigue capturada.
        vault_storage[key] = value

    def recall(key: str) -> Any:
        """
        Recupera un valor de la bóveda o indica que no existe.
        """
        return vault_storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall}


if __name__ == "__main__":
    # 1. Prueba de mage_counter
    # Demuestra que dos contadores tienen estados independientes [2]
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    # 2. Prueba de spell_accumulator
    # Demuestra la acumulación de poder sobre una base [3, 5]
    print("\nTesting spell accumulator...")
    base_power = 100
    acc = spell_accumulator(base_power)
    print(f"Base 100, add 20: {acc(20)}")  # Debe imprimir 120
    print(f"Total 120, add 30: {acc(30)}")  # Debe imprimir 150

    # 3. Prueba de enchantment_factory
    # Demuestra la creación de funciones personalizadas [4, 5]
    print("\nTesting enchantment factory...")
    fire_factory = enchantment_factory("Flaming")
    ice_factory = enchantment_factory("Frozen")
    print(fire_factory("Sword"))   # Debe imprimir "Flaming Sword"
    print(ice_factory("Shield"))   # Debe imprimir "Frozen Shield"

    # 4. Prueba de memory_vault
    # Demuestra el almacenamiento privado y compartido [3, 4]
    print("\nTesting memory vault...")
    vault = memory_vault()

    # Usamos las claves del diccionario retornado
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)

    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
