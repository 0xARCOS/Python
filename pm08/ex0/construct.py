import sys
import os
import site


def check_the_construct():
    is_venv = sys.prefix != sys.base_prefix

    if is_venv:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        print(f"Site-Packages: {site.getsitepackages()[0]}")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Environment Path: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_ven")
        print("source matrix_env/bin/activate # On Unix")
        print(".\\matrix_venv\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")


if __name__ == "__main__":
    check_the_construct()
