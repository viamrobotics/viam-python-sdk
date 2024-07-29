import re
import sys

from typing import Literal, Union


def update_version(file_path: str, version_type: Union[Literal["api"], Literal["sdk"]], new_version: str):
    with open(file_path, "r") as file:
        data = file.read()

    if version_type.lower() == "api":
        version = r'(API_VERSION\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"'
    elif version_type.lower() == "sdk":
        version = r'(SDK_VERSION\s*=\s*)"[0-9]+\.[0-9]+\.[0-9]+"'
    else:
        print("version_type must be either 'api' or 'sdk'")
        sys.exit(1)

    data = re.sub(version, f'\\1"{new_version}"', data)

    with open(file_path, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 etc/update_version.py <file_path> sdk|api <new_version>")
        sys.exit(1)

    update_version(sys.argv[1], sys.argv[2], sys.argv[3])
