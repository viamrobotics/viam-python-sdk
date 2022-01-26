from gettext import find
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='viam',
    version='0.0.1',
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
    packages=find_packages(),
    python_requires='>=3.6, <4',
    install_requires=['grpclib'],
)
