import re
import sys


file_path = "pyproject.toml"


def update_version(new_version: str):
    with open(file_path, "r") as file:
        data = file.read()

    data = re.sub(
        r'(api_version\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"',
        f'\\1"{new_version}"',
        data
    )

    with open(file_path, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(len(sys.argv), sys.argv)
        print("Usage: python update_version.py <new_version>")
        sys.exit(1)

    update_version(sys.argv[1])
