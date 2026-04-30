import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f: typing.IO[str] = open(filename, 'r')
        content: str = f.read()
        f.close()

        print("---\n")
        print(content, end="")
        print("\n---")
        print(f"File '{filename}' closed.")
        print("Transform data:")
        print("---")

        lines: typing.List[str] = content.split('\n')
        new_content: str = ""

        for line in lines:
            if len(line) > 0:
                new_line: str = line + "#\n"
                new_content = new_content + new_line
                print(new_line, end="")

        print("---")

        save_name: str = input("Enter new file name (or empty): ")

        if len(save_name) == 0:
            print("Not saving data.")
        else:
            print(f"Saving data to '{save_name}'")
            f_new: typing.IO[str] = open(save_name, 'w')
            f_new.write(new_content)
            f_new.close()
            print(f"Data saved in file '{save_name}'.")

    except OSError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
