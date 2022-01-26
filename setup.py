import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='viam',
    version='0.0.1',
    author='Viam',
    author_email='naveed@viam.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/viamrobotics/python-sdk',
    project_urls={
        "Bug Tracker": "https://github.com/viamrobotics/python-sdk/issues"
    },
    packages=['viam'],
    install_requires=['grpclib'],
)
