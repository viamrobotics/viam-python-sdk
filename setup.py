from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='viam-python-sdk',
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
    packages=['viam'],
    python_requires='>=3.6, <4',
    install_requires=['grpclib'],
)
