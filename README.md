<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=3FB950&center=true&vCenter=true&width=600&lines=Python+Learning+Path;42+curriculum;70%2B+Ejercicios+Progresivos" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Modules](https://img.shields.io/badge/M%C3%B3dulos-10-3FB950?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-Activo-brightgreen?style=for-the-badge)

<br/>

> **Currículo progresivo de Python**: desde los fundamentos hasta patrones de diseño avanzados y programación funcional,
> con una temática narrativa de jardines, criaturas y magia que evoluciona a lo largo del curso.

</div>

---

## 📚 Índice de Módulos

| Módulo | Tema | Conceptos clave |
|--------|------|-----------------|
| [PM00](#pm00--fundamentos-de-python) | Fundamentos | `print`, variables, condicionales, bucles, recursión |
| [PM01](#pm01--funciones-y-clases) | OOP básico | Clases, métodos, herencia, Factory Pattern |
| [PM02](#pm02--manejo-de-excepciones) | Excepciones | `try/except/finally`, excepciones custom |
| [PM03](#pm03--estructuras-de-datos) | Datos | Dicts, sets, `sys.argv`, generators |
| [PM04](#pm04--entrada--salida-de-archivos) | I/O | Archivos, `with`, `sys.stdin/stdout/stderr` |
| [PM05](#pm05--clases-abstractas-y-polimorfismo) | ABCs | `abc`, polimorfismo, Protocol |
| [PM07](#pm07--patrones-de-diseño) | Design Patterns | Abstract Factory, Mixin, Strategy |
| [PM08](#pm08--entornos-y-dependencias) | Entornos | `venv`, `pip`, `poetry`, `.env`, `logging` |
| [PM09](#pm09--pydantic) | Validación | Pydantic v2, `BaseModel`, `Field`, `model_validator` |
| [PM10](#pm10--programación-funcional) | Funcional | Lambdas, closures, `functools`, decoradores |

---

## PM00 — Fundamentos de Python

<details>
<summary><b>9 ejercicios · click para expandir</b></summary>

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

📖 [README detallado de PM00](pm00/README.md)

</details>

---

## PM01 — Funciones y Clases

<details>
<summary><b>7 ejercicios · click para expandir</b></summary>

Introducción a la Programación Orientada a Objetos. Clase `Plant` con atributos, métodos, herencia y encapsulación.

| Archivo | Descripción |
|---|---|
| `ft_garden_intro.py` | Visualización básica de datos |
| `ft_garden_data.py` | Manejo de datos estructurados |
| `ft_plant_growth.py` | Simulaciones de crecimiento |
| `ft_plant_factory.py` | **Factory Pattern** — creación de objetos |
| `ft_garden_security.py` | Encapsulación y acceso controlado |
| `ft_plant_types.py` | Herencia y jerarquía de tipos |
| `ft_garden_analytics.py` | Análisis estadístico, clases anidadas |

📖 [README detallado de PM01](pm01/README.md)

</details>

---

## PM02 — Manejo de Excepciones

<details>
<summary><b>6 ejercicios · click para expandir</b></summary>

Control de flujo ante errores. Desde `try/except` básico hasta jerarquías de excepciones propias.

| Archivo | Descripción |
|---|---|
| `ft_first_exception.py` | `try/except` básico con validación |
| `ft_different_errors.py` | Múltiples tipos de excepción |
| `ft_custom_errors.py` | Clases de excepción propias |
| `ft_finally_block.py` | Uso del bloque `finally` |
| `ft_raise_errors.py` | Lanzar y propagar excepciones |
| `ft_garden_management.py` | Sistema completo con excepciones custom |

📖 [README detallado de PM02](pm02/README.md)

</details>

---

## PM03 — Estructuras de Datos

<details>
<summary><b>7 ejercicios · click para expandir</b></summary>

Diccionarios, conjuntos y colecciones avanzadas. Generadores y argumentos CLI con `sys.argv`.

| Archivo | Descripción |
|---|---|
| `ft_command_quest.py` | Argumentos CLI con `sys.argv` |
| `ft_score_analytics.py` | Estadísticas con listas |
| `ft_coordinate_system.py` | Tuplas y distancias 3D |
| `ft_achievement_tracker.py` | Operaciones con conjuntos (sets) |
| `ft_inventory_system.py` | Diccionarios avanzados |
| `ft_data_stream.py` | Generadores con `yield` |
| `ft_data_alchemist.py` | List/dict comprehensions |

📖 [README detallado de PM03](pm03/README.md)

</details>

---

## PM04 — Entrada / Salida de Archivos

<details>
<summary><b>4 ejercicios · click para expandir</b></summary>

Lectura, escritura y transformación de archivos. Gestión segura de recursos con context managers.

| Archivo | Descripción |
|---|---|
| `ft_ancient_text.py` | Lectura con manejo de errores |
| `ft_archive_creation.py` | Leer → transformar → escribir |
| `ft_stream_management.py` | `sys.stdin/stdout/stderr` |
| `ft_vault_security.py` | `with` statement obligatorio |

📖 [README detallado de PM04](pm04/README.md)

</details>

---

## PM05 — Clases Abstractas y Polimorfismo

<details>
<summary><b>3 ejercicios · click para expandir</b></summary>

El módulo `abc` para definir interfaces. Despacho polimórfico con un pipeline de datos real.

| Archivo | Descripción |
|---|---|
| `data_processor.py` | ABCs: `NumericProcessor`, `TextProcessor`, `LogProcessor` |
| `data_stream.py` | `DataStream` enruta datos al procesador correcto |
| `data_pipeline.py` | Pipeline completo + `Protocol` para plugins |

📖 [README detallado de PM05](pm05/README.md)

</details>

---

## PM07 — Patrones de Diseño

<details>
<summary><b>13 ejercicios · click para expandir</b></summary>

El módulo más avanzado del Common Core. Implementa tres patrones clásicos con un sistema de criaturas y batallas.

#### `ex0` — Abstract Factory Pattern

```
CreatureFactory (abstracta)
    ├── FlameFactory  →  Flameling, Pyrodon
    └── AquaFactory   →  Aquabub, Torragon
```

#### `ex1` — Mixin Pattern

```
HealCapability    ──► Sproutling, Bloomelle
TransformCapability ─► Shiftling, Morphagon
```

#### `ex2` — Strategy Pattern

```python
creature.set_strategy(AggressiveStrategy())
creature.execute()   # transforma y ataca

creature.set_strategy(DefensiveStrategy())
creature.execute()   # cura y defiende
```

📖 [README detallado de PM07](pm07/README.md)

</details>

---

## PM08 — Entornos y Dependencias

<details>
<summary><b>3 ejercicios · click para expandir</b></summary>

Gestión de entornos virtuales, paquetes externos y configuración segura de secretos.

| Archivo | Descripción |
|---|---|
| `construct.py` | Detección de `venv` y entorno activo |
| `loading.py` | `pandas`, `numpy`, `matplotlib` + `poetry` vs `pip` |
| `oracle.py` | Variables de entorno con `python-dotenv` y `logging` |

📖 [README detallado de PM08](pm08/README.md)

</details>

---

## PM09 — Pydantic

<details>
<summary><b>3 ejercicios · click para expandir</b></summary>

Validación declarativa de datos con Pydantic v2. Modelos, campos con constraints y validadores de negocio.

| Archivo | Descripción |
|---|---|
| `space_station.py` | `BaseModel` y `Field` con constraints básicos |
| `alien_contact.py` | `Enum`, `Optional`, `model_validator` |
| `space_crew.py` | Modelos anidados, listas validadas, reglas complejas |

📖 [README detallado de PM09](pm09/README.md)

</details>

---

## PM10 — Programación Funcional

<details>
<summary><b>5 ejercicios · click para expandir</b></summary>

El cierre del Common Core. Programación funcional completa: lambdas, closures, `functools` y decoradores.

| Archivo | Descripción |
|---|---|
| `lambda_spells.py` | `lambda`, `filter()`, `map()`, `sorted()` |
| `higher_magic.py` | Higher-order functions — funciones que devuelven funciones |
| `scope_mistery.py` | Closures, `nonlocal`, estado privado |
| `functools_artifacts.py` | `reduce`, `partial`, `lru_cache`, `singledispatch` |
| `decorador_mastery.py` | Decoradores con y sin argumentos, `@wraps` |

📖 [README detallado de PM10](pm10/README.md)

</details>

---

## Requisitos

- **Python 3.10+** — sin dependencias externas (salvo PM08/PM09 que usan librerías externas)
- PM00–PM07: solo librería estándar (`sys`, `abc`, `typing`, `random`, `math`)
- PM08: `pandas`, `numpy`, `matplotlib`, `python-dotenv`
- PM09: `pydantic>=2.0`
- PM10: solo librería estándar (`functools`, `time`)

---

<div align="center">

**70+ ejercicios · 10 módulos · Common Core completo**

</div>
