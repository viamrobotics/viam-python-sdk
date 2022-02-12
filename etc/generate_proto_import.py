import os
from pathlib import Path
import re
import shutil
from typing import List, Dict


# Name of the package where the protos are built
PROTO_GEN_PACKAGE = 'gen'

# The path where BUF builds the proto files
GENERATED_PATH = Path(__file__).parent.parent / 'viam' / PROTO_GEN_PACKAGE

# The path where we would like to import from
NEW_IMPORT_PATH = GENERATED_PATH.parent / 'proto'


def clean():
    '''
    Delete all the files in the NEW_IMPORT_PATH
    '''
    shutil.rmtree(NEW_IMPORT_PATH)


def get_packages(root: str) -> Dict[str, List[str]]:
    '''
    Get all the packages/modules/files.

    Organized as a dictionary
    Key: package name
    Value: array of modules/files
    '''
    packages: Dict[str, List[str]] = {}

    for (dirpath, _, filenames) in os.walk(root):
        if '__' in dirpath:
            continue
        if filenames:
            rel_path = Path(dirpath).relative_to(root).__str__()
            rel_path = rel_path.replace(os.path.sep, '.')
            packages[rel_path] = list(
                set([f.split('.')[0] for f in filenames]))
    return packages


def build_dirs(root: str, package: str, modules: List[str]):
    '''
    Build the directory and file structure for the new proto imports.

    Example:
    We want to the protobuf/grpc definitions from

        viam.gen.proto.api.component.imu_grpc
        viam.gen.proto.api.component.imu_pb2

    to be available at

        viam.proto.api.component.imu

    This function will take in the directory where to store the new imports,
    the package name, and the modules (files) within that package.

    Then, it will create the appropriate directory structure, and a new
    file for each module type (e.g. "imu" for "imu_grpc" and "imu_pb2").
    '''
    # Create new directory/ies
    dir_name = os.path.sep.join(package.split('.')[:-1])
    dir_name = os.path.join(root, dir_name)
    os.makedirs(dir_name, exist_ok=True)

    # Get a list of all the new file names (grpc and pb2 combined)
    mods = list(set([mod.replace('_grpc', '').replace('_pb2', '')
                for mod in modules]))
    for mod in mods:

        # Get list of only the files we want to import from,
        # based on the new module name
        imports = list(filter(lambda n: mod in n, modules))

        # We only want to import classes. This could be accomplished with
        # from ... import *
        # but `import *` is discouraged
        classes = {}

        # regex for matching only classnames, ignoring any nested classes
        class_match = re.compile(
            r'^\s{0}class\s+(?P<class_name>\w+)(\(.+\))?:'
        )
        for imp in imports:
            if '_grpc' in imp:
                f_name = f'{imp}.py'
            elif '_pb2' in imp:
                f_name = f'{imp}.pyi'
            else:
                continue

            f_path = os.path.join(
                GENERATED_PATH.__str__(),
                package.replace('.', os.path.sep),
                f_name
            )
            class_names = []
            with open(f_path, 'r') as f:
                for line in f.readlines():
                    for match in re.finditer(class_match, line):
                        class_name = match.group('class_name')
                        if class_name.startswith('_'):
                            continue
                        class_names.append(class_name)

            classes[imp] = class_names

        # Write new import to disk
        with open(os.path.join(dir_name, f'{mod}.py'), 'w') as f:
            f.write("'''\n")
            f.write('**** THIS IS A GENERATED FILE ****\n')
            f.write('********** DO NOT EDIT ***********\n')
            f.write("'''\n")
            for (imp, cls) in classes.items():
                f.write(
                    f'from {"."*len(package.split("."))}{PROTO_GEN_PACKAGE}.' +
                    f'{package}.{imp} import (\n'
                )
                f.write('    %s\n' % (',\n    '.join(cls)))
                f.write(')\n')


def run():
    clean()
    packages = get_packages(GENERATED_PATH.__str__())
    for (package, modules) in packages.items():
        build_dirs(NEW_IMPORT_PATH.parent.__str__(), package, modules)


if __name__ == '__main__':
    run()
