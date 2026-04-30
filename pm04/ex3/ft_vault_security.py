# Ex3: solo open(), read(), write(), print() autorizados
# No sys, no typing — usamos tipos nativos de Python 3.10+
# OBLIGATORIO usar 'with' statement aquí


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    """
    Lee o escribe un archivo de forma segura.
    'with' garantiza que el archivo se cierra siempre,
    incluso si ocurre una excepción dentro del bloque.
    Retorna (True, contenido) o (False, mensaje_error).
    """
    try:
        if action == "read":
            # 'with open(...) as f:' → f.close() automático al salir
            with open(filename, 'r') as f:
                return (True, f.read())
        else:
            with open(filename, 'w') as f:
                f.write(content)
                return (True, 'Content successfully written to file')
    except OSError as e:
        # str(e) convierte el error a su mensaje legible
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/shadow'))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive('ancient_fragment.txt')
    print(result)

    print(
        "Using 'secure_archive' to write previous content to a new file:"
    )
    if result[0]:
        print(secure_archive('output_fragment.txt', 'write', result[1]))


if __name__ == "__main__":
    main()
