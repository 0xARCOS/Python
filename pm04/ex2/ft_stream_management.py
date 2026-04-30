import sys
import typing


def main() -> None:
    """Manage data streams for archive preservation."""
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
        return

    filename: str = sys.argv[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    try:
        # Lectura del archivo original
        f: typing.IO[str] = open(filename, 'r')
        content: str = f.read()
        f.close()

        sys.stdout.write("---\n")
        sys.stdout.write(content)
        if not content.endswith('\n'):
            sys.stdout.write("\n")
        sys.stdout.write("---\n")
        sys.stdout.write(f"File '{filename}' closed.\n")

        # Transformación de datos
        sys.stdout.write("Transform data:\n")
        sys.stdout.write("---\n")
        lines: typing.List[str] = content.split('\n')
        new_content: str = ""
        for line in lines:
            if len(line) > 0:
                new_line: str = line + "#\n"
                new_content = new_content + new_line
                sys.stdout.write(new_line)
        sys.stdout.write("---\n")

        # Reemplazo de input() por sys.stdin
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        # readline() captura el \n del Enter, hay que limpiarlo
        save_name_raw: str = sys.stdin.readline()
        save_name: str = save_name_raw.replace('\n', '')

        if len(save_name) == 0:
            sys.stdout.write("Not saving data.\n")
        else:
            try:
                sys.stdout.write(f"Saving data to '{save_name}'\n")
                f_new: typing.IO[str] = open(save_name, 'w')
                f_new.write(new_content)
                f_new.close()
                sys.stdout.write(f"Data saved in file '{save_name}'.\n")
            except OSError as e:
                # Error al guardar va a STDERR (Acortado para E501)
                err_msg = f"[STDERR] Error opening file '{save_name}': {e}\n"
                sys.stderr.write(err_msg)
                sys.stdout.write("Data not saved.\n")

    except OSError as e:
        # Error al abrir original va a STDERR
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")


if __name__ == "__main__":
    main()
