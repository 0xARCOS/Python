import sys
import importlib.metadata


def main() -> None:
    # Definimos las librerías necesarias para el ejercicio
    libraries = ["pandas", "numpy", "matplotlib"]

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    # Verificación de dependencias y versiones
    try:
        for lib in libraries:
            # Obtenemos la versión de cada paquete instalado
            version = importlib.metadata.version(lib)
            print(f"[OK] {lib} ({version}) - Ready")

        # Importaciones una vez confirmadas las dependencias
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except (importlib.metadata.PackageNotFoundError, ImportError):
        print("\n[MISSING] - Dependencia no encontrada.")
        print("Instala con: pip install -r requirements.txt")
        print("O con: poetry install")
        sys.exit(1)

    # 1. Generar datos con numpy: valores numéricos + categorías aleatorias
    n = 1000
    valores = np.random.normal(50, 15, n)
    category_list: list = ['Sentinels', 'Zion', 'Agents', 'Programs']
    categorias = np.random.choice(category_list, n)

    # 2. Meter todo en un DataFrame de pandas
    df = pd.DataFrame({'Signal': valores, 'Group': categorias})

    # 3. Calcular estadísticas con df.describe()
    print("\n--- ESTADÍSTICAS ---")
    print(df.describe())

    # 4. Filtrar por categoría (Media de cada grupo)
    print("\n--- MEDIA POR GRUPO ---")
    # Usamos numeric_only=True para evitar advertencias de pandas
    print(df.groupby('Group').mean(numeric_only=True))

    # 5. Visualizar con un histograma en matplotlib
    print("\nGenerando visualización...")
    df.hist(
        by='Group',
        column='Signal',
        figsize=(10, 8),
        bins=20,
        color='green',
        edgecolor='black'
    )

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    # Requisito de la misión: Breve comparación final
    print("\n--- PIP vs POETRY ---")
    print("Pip usa requirements.txt (simple/estándar).")
    print("Poetry usa pyproject.toml \
            (gestión de entornos y versiones determinista).")
    print("\n¡Listo! Imagen guardada como 'matrix_analysis.png'")


if __name__ == "__main__":
    main()
