import re
import sys


def update_version(file_path: str, new_version: str):
    with open(file_path, "r") as file:
        data = file.read()

    data = re.sub(
        r'(API_VERSION\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"',
        f'\\1"{new_version}"',
        data
    )

    with open(file_path, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python etc/update_version.py <file_path> <new_version>")
        sys.exit(1)

    update_version(sys.argv[1], sys.argv[2])
