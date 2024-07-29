import re
import sys


def update_version(file_path: str, version_type: str, new_version: str):
    with open(file_path, "r") as file:
        data = file.read()

    if version_type == "api":
        data = re.sub(
            r'(API_VERSION\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"',
            f'\\1"{new_version}"',
            data
        )
    elif version_type == "sdk":
        data = re.sub(
            r'(SDK_VERSION\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"',
            f'\\1"{new_version}"',
            data
        )
    else:
        print("version_type must be either 'api' or 'sdk'")
        sys.exit(1)

    with open(file_path, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 etc/update_version.py <file_path> sdk|api <new_version>")
        sys.exit(1)

    update_version(sys.argv[1], sys.argv[2], sys.argv[3])
