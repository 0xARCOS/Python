import sys


class ErrorManager(Exception):
    """clase para manejar los diferentes tipos de errores"""
    pass


class ZeroArgv(ErrorManager):
    """Error que maneja el argumento vacío"""
    pass


def main(args: list[str]) -> None:
    print("=== Comand Quest ===")
    print(f"Program name: {args[0]}")

    try:
        if len(args) == 1:
            raise ZeroArgv

        print(f"Arguments received: {len(args) - 1}")

        i = 1
        while i < len(args):
            print(f"Argument {i}: {args[i]}")
            i += 1

        print(f"Total arguments: {len(args)}")
    except ZeroArgv:
        print("No arguments provided!")
        print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main(sys.argv)
