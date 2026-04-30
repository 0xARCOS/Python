import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit()
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery")
    print(f"Accessing file '{filename}'")
    try:
        f: typing.IO[str] = open(filename)
        content: str = f.read()
        f.close()
        print("---")
        print(content, end="")
        print("---")
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
