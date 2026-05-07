<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=3FB950&center=true&vCenter=true&width=600&lines=Python+Learning+Path;42+curriculum;49+Ejercicios+Progresivos" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Modules](https://img.shields.io/badge/M%C3%B3dulos-7-3FB950?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Ejercicios-49-FF6B6B?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen?style=for-the-badge)

<br/>

> **Currículo progresivo de Python**: desde los fundamentos hasta patrones de diseño avanzados,
> con una temática narrativa de jardines y criaturas que evoluciona a lo largo del curso.

</div>

---

## Módulos

<details>
<summary><b>PM00 — Fundamentos de Python</b> · 9 ejercicios</summary>

<br/>

Primer contacto con Python. Operaciones básicas, entrada/salida, condicionales y recursión, todo ambientado en un jardín.

| Archivo | Descripción |
|---|---|
| `ft_hello_garden.py` | Primer `print` — bienvenida al jardín |
| `ft_plot_area.py` | Entrada del usuario y aritmética básica |
| `ft_harvest_total.py` | Formateo de strings |
| `ft_plant_age.py` | Manipulación de variables |
| `ft_water_reminder.py` | Lógica condicional |
| `ft_count_harvest_iterative.py` | Bucles e iteración |
| `ft_count_harvest_recursive.py` | Recursión |
| `ft_garden_summary.py` | Operaciones de resumen |
| `ft_seed_inventory.py` | Gestión básica de inventario |

```python
# Ejemplo — recursión
def count_harvest(n):
    if n <= 0:
        return 0
    return n + count_harvest(n - 1)
```

</details>

---

<details>
<summary><b>PM01 — Funciones y Clases</b> · 7 ejercicios</summary>

<br/>

Introducción a la Programación Orientada a Objetos. Se introduce la clase `Plant` con atributos, métodos y el patrón Factory por primera vez.

| Archivo | Descripción |
|---|---|
| `ft_garden_intro.py` | Visualización básica de datos |
| `ft_garden_data.py` | Manejo de datos estructurados |
| `ft_plant_growth.py` | Simulaciones de crecimiento |
| `ft_plant_factory.py` | **Factory Pattern** — creación de objetos `Plant` |
| `ft_garden_security.py` | Encapsulación y acceso controlado |
| `ft_plant_types.py` | Herencia y jerarquía de tipos |
| `ft_garden_analytics.py` | Análisis estadístico de datos |

```python
# Primer acercamiento al patrón Factory
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
```

</details>

---

<details>
<summary><b>PM02 — Manejo de Excepciones</b> · 6 ejercicios</summary>

<br/>

Control de flujo ante errores. Desde `try/except` básico hasta excepciones personalizadas con jerarquías propias.

| Archivo | Descripción |
|---|---|
| `ft_first_exception.py` | `try/except` básico con validación de temperatura |
| `ft_different_errors.py` | Manejo de múltiples tipos de excepción |
| `ft_custom_errors.py` | Creación de clases de excepción propias |
| `ft_finally_block.py` | Uso del bloque `finally` |
| `ft_raise_errors.py` | Lanzar y propagar excepciones |
| `ft_garden_management.py` | Sistema completo con `GardenManager` y excepciones propias |

```python
# Excepciones personalizadas
class InvalidPlantError(Exception): ...
class WaterLevelError(Exception): ...
class PlantNotFoundError(Exception): ...

class GardenManager:
    def water_plant(self, name: str, amount: float):
        if amount < 0:
            raise WaterLevelError("El nivel de agua no puede ser negativo")
```

</details>

---

<details>
<summary><b>PM03 — Estructuras de Datos</b> · 7 ejercicios</summary>

<br/>

Diccionarios, conjuntos y colecciones avanzadas. Manejo de argumentos por línea de comandos con `sys.argv`.

| Archivo | Descripción |
|---|---|
| `ft_command_quest.py` | Argumentos CLI con gestión de errores custom |
| `ft_score_analytics.py` | Sistemas de puntuación y estadísticas |
| `ft_coordinate_system.py` | Gestión de coordenadas con diccionarios |
| `ft_achievement_tracker.py` | Sistema de logros con conjuntos |
| `ft_inventory_system.py` | Inventario avanzado con porcentajes |
| `ft_data_stream.py` | Procesamiento de flujos de datos |
| `ft_data_alchemist.py` | Transformación y manipulación de datos |

```python
# Inventario con argumentos CLI
import sys

inventory = {}
for item in sys.argv[1:]:
    inventory[item] = inventory.get(item, 0) + 1
```

</details>

---

<details>
<summary><b>PM04 — Entrada/Salida de Archivos</b> · 4 ejercicios</summary>

<br/>

Lectura, escritura y transformación de archivos. Gestión segura de recursos con context managers.

| Archivo | Descripción |
|---|---|
| `ft_ancient_text.py` | Lectura de archivos con manejo de errores |
| `ft_archive_creation.py` | Leer → transformar → escribir nuevos archivos |
| `ft_stream_management.py` | Gestión de streams y buffers |
| `ft_vault_security.py` | Operaciones de archivo seguras |

```python
# Leer, transformar y guardar
with open(source, 'r') as f:
    lines = f.readlines()

with open(destination, 'w') as f:
    for line in lines:
        f.write(f"# {line}")
```

</details>

---

<details>
<summary><b>PM05 — Clases Abstractas y Polimorfismo</b> · 3 ejercicios</summary>

<br/>

El módulo `abc` de Python para definir interfaces. Despacho polimórfico con un pipeline de datos real.

| Archivo | Descripción |
|---|---|
| `data_processor.py` | ABCs: `NumericProcessor`, `TextProcessor`, `LogProcessor` |
| `data_stream.py` | `DataStream` enruta datos al procesador correcto |
| `data_pipeline.py` | Pipeline completo de transformación |

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: str) -> str: ...

class NumericProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return str(float(data) * 2)
```

</details>

---

<details>
<summary><b>PM07 — Patrones de Diseño</b> · 13 ejercicios</summary>

<br/>

El módulo más avanzado del currículo. Implementa tres patrones clásicos de diseño con un sistema de criaturas y batallas.

Las criaturas tienen tipos elementales (Fuego / Agua / Planta) con estadísticas de ataque, defensa y habilidades especiales.

---

#### `ex0` — Factory Pattern

Cada familia de criaturas tiene su propia fábrica concreta.

```
CreatureFactory (abstracta)
    ├── FlameFactory  →  Flameling, Pyrodon
    └── AquaFactory   →  Aquabub, Torragon
```

```python
class FlameFactory(CreatureFactory):
    def create_basic(self) -> Creature:
        return Flameling()
    def create_advanced(self) -> Creature:
        return Pyrodon()
```

---

#### `ex1` — Decorator / Mixin Pattern

Capacidades adicionales mezcladas en las criaturas en tiempo de diseño.

```
HealCapability   ──┬──► Sproutling (Heal)
                   └──► Bloomelle  (Heal)
TransformCapability─┬──► Shiftling  (Transform)
                    └──► Morphagon  (Transform)
```

---

#### `ex2` — Strategy Pattern

El comportamiento de combate se intercambia en tiempo de ejecución.

```python
creature.set_strategy(AggressiveStrategy())
creature.execute()   # ataca con toda la fuerza

creature.set_strategy(DefensiveStrategy())
creature.execute()   # prioriza la defensa
```

| Archivo | Patrón |
|---|---|
| `ex0/creature.py` | Abstract Factory — interfaz base |
| `ex0/creatures.py` | Concrete Factories y productos |
| `ex1/capability.py` | Mixin interfaces |
| `ex1/creatures.py` | Criaturas con capacidades mezcladas |
| `ex1/factory.py` | Factories con soporte de mixins |
| `ex2/base_strategy.py` | Strategy — clases base |
| `ex2/strategies.py` | Estrategias concretas |
| `ex2/exceptions.py` | Excepciones del sistema de estrategias |
| `battle.py` | Sistema de batalla — prueba Factory Pattern |
| `capacitor.py` | Prueba avanzada de capacidades y transformaciones |

</details>

---
---

## Requisitos

- **Python 3.x** — sin dependencias externas
- Todos los módulos usan únicamente la librería estándar: `sys`, `abc`, `typing`

---

<div align="center">

**49 ejercicios · 7 módulos**

</div>
