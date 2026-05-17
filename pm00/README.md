# PM00 — Fundamentos de Python

> **Temática:** Un jardín. Eres el jardinero. Python es tu herramienta.

---

## 🧠 Teoría del módulo

### ¿Por qué Python después de C?

Venís de C, donde todo es explícito: declaras el tipo, gestionas la memoria, manejas el puntero. Python invierte eso: el intérprete se encarga de todo eso por ti. El precio que pagas es velocidad; la ganancia es expresividad.

Diferencias clave respecto a C:

| C | Python |
|---|--------|
| `int x = 5;` | `x = 5` |
| `printf("%d\n", x)` | `print(x)` |
| `scanf("%d", &x)` | `x = input()` |
| Tipado estático | Tipado dinámico |
| Gestión manual de memoria | Garbage collector |
| Compilado | Interpretado |

### Variables y tipos básicos

```python
# Python infiere el tipo automáticamente
x = 5          # int
y = 3.14       # float
name = "Rose"  # str
is_ok = True   # bool

# Puedes cambiar el tipo en cualquier momento (tipado dinámico)
x = "ahora soy string"  # válido en Python, ilegal en C
```

### `print()` e `input()`

```python
# print() acepta cualquier tipo y lo convierte a string
print("Hola")          # Hola
print(42)              # 42
print(f"Valor: {42}")  # f-strings: la forma moderna de formatear

# input() SIEMPRE devuelve string — hay que convertir
age = input("Tu edad: ")   # "25" (string)
age = int(age)             # 25 (int)
# O en una línea:
age = int(input("Tu edad: "))
```

### Condicionales

```python
# Python usa indentación en lugar de llaves {}
if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")

# No hay switch/case hasta Python 3.10 (match/case)
```

### Bucles

```python
# for — itera sobre cualquier "iterable"
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

# while — igual que en C
i = 0
while i < 5:
    print(i)
    i += 1
```

### Recursión

En Python la recursión funciona igual que en C, pero hay un límite de profundidad (~1000 llamadas por defecto). Para problemas grandes, los bucles son más seguros.

```python
def countdown(n):
    if n <= 0:          # caso base — SIEMPRE necesario
        return
    print(n)
    countdown(n - 1)    # llamada recursiva
```

### f-strings (formateo moderno)

```python
name = "Rose"
height = 25
# Forma antigua (C-style)
print("Plant: %s, Height: %d" % (name, height))
# Forma nueva — f-strings (Python 3.6+)
print(f"Plant: {name}, Height: {height}cm")
# Puedes poner expresiones dentro
print(f"Double height: {height * 2}cm")
```

---

## 📁 Ejercicios

### ex0 — `ft_hello_garden.py`
**Objetivo:** Tu primer `print` en Python.

```python
def ft_hello_garden():
    print("Hello, Garden Community!")
```

**Razonamiento:** Solo entender que en Python las funciones se definen con `def` y que `print()` no necesita `\n` al final (lo añade automáticamente).

---

### ex1 — `ft_plot_area.py`
**Objetivo:** Leer dos números y multiplicarlos.

**Razonamiento:**
1. `input()` devuelve string → hay que convertir con `int()`
2. Multiplicar y mostrar resultado con f-string

```python
a = int(input("Enter length: "))
b = int(input("Enter width: "))
print(f"Plot area: {a * b}")
```

---

### ex2 — `ft_harvest_total.py`
**Objetivo:** Leer tres valores y operar con ellos.

**Razonamiento:** Igual que ex1 pero con tres variables. Practica la repetición del patrón `int(input(...))`.

---

### ex3 — `ft_plant_age.py`
**Objetivo:** Primera condicional.

**Razonamiento:** Si días > 60 → listo para cosechar. El patrón `if/else` es idéntico a C salvo la indentación y los dos puntos `:`.

---

### ex4 — `ft_water_reminder.py`
**Objetivo:** Condicional con umbral.

**Razonamiento:** Mismo patrón que ex3. La diferencia es el contexto: días desde el último riego.

---

### ex5 — `ft_count_harvest_iterative.py` y `ft_count_harvest_recursive.py`
**Objetivo:** Implementar el mismo countdown de dos formas.

**Razonamiento (iterativo):** Un `for` con `range(1, days)` imprime cada día, y después "Harvest time!".

**Razonamiento (recursivo):**
```
count_current(1)
  → imprime 1
  → count_current(2)
       → imprime 2
       → ...
            → count_current(days)
                 → imprime days
                 → imprime "Harvest time!"
                 → return
```

La clave: la función interna `count_current` es un closure que captura `days` del ámbito exterior. Esto es un anticipo de PM10.

---

### ex6 — `ft_garden_summary.py`
**Objetivo:** Múltiples `input()` y formateo de salida.

**Razonamiento:** Practica pedir varios datos y mostrarlos formateados. No hay lógica nueva — consolida lo anterior.

---

### ex7 — `ft_seed_inventory.py`
**Objetivo:** Función con parámetros y condicional múltiple.

**Razonamiento:** Primera función con argumentos tipados. El `unit` determina el formato del mensaje. Introduce `str.capitalize()`.

```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()  # "rose" → "Rose"
    if unit == "packets":
        print(f"{seed} seeds: {quantity} packets available")
    elif unit == "grams":
        ...
```

---

## ✅ Checklist de conceptos dominados

- [ ] `print()` con f-strings
- [ ] `input()` + conversión de tipos
- [ ] `if / elif / else`
- [ ] `for` con `range()`
- [ ] `while`
- [ ] Recursión con caso base
- [ ] Funciones con parámetros y tipo de retorno
- [ ] `str.capitalize()`
