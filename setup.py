import os
import pathlib
from typing import List

from setuptools import find_packages, setup

import viam

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


def get_packages(root: str) -> List[str]:
    packages: List[str] = []

    for (dirname, dirpaths, _) in os.walk(root):
        packages.append(dirname.replace(os.path.sep, '.'))

    return packages


setup(
    name='viam',
    version=viam.__version__,
    author='Viam',
    author_email='naveed@viam.com',
    description='Viam Python SDK to connect to robots running the Viam RDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/viamrobotics/python-sdk',
    project_urls={
        'Bug Tracker': 'https://github.com/viamrobotics/python-sdk/issues',
    },
    keywords='robotics, robots',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=(
        find_packages() +
        get_packages(os.path.join('.', 'viam', 'gen')) +
        get_packages(os.path.join('.', 'viam', 'proto'))
    ),
    package_data={
        '': ['py.typed', '*.pyi', '**/*.pyi'],
    },
    python_requires='>=3.6, <4',
    install_requires=[
        'grpclib',
        'protobuf',
        'googleapis-common-protos',
        'Pillow',
        'typing-extensions',
    ],
)
