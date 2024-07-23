import re


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
