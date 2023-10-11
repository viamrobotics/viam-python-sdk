# Viam + Python

This guide will help you get set up with Viam with Python. It assumes that you are starting from scratch, and will walk you through setting up a fresh environment and installing the necessary requirements.

## Setup your project

The first step is to create a directory to house your project. For this guide, we will be using the directory name `viam-python`:

```bash
mkdir viam-python
cd viam-python
```

## Create a Virtual Environment

Now that we are in the project directory, let's create and activate a virtual environment for python to run in.

> **INFO**
> Creating a virtual environment (`venv`) is important as it isolates this python environment from any other you might already have. This allows us to ensure a clean project and easier dependency management, and it avoids bloating your global python environment.

```bash
python3 -m venv viam-env
source viam-env/bin/activate
```

> **NOTE**
> Some Linux environments may not have the necessary requirements to create a virtual environment. If you receive an error, you can try running `apt install python3-venv` and then running the above commands.

You will now see `(viam-env)` prepend the commands in your terminal window. This shows that the python packages being used are from this particular environment.

You can exit this environment by running `deactivate`.

## Install Viam

Inside the activated `viam-env` python environment, you can now install the Viam SDK:

```bash
pip3 install viam-sdk
```

This will install Viam and all required dependencies.

Should you need to install your own requirements, be sure to do so in this environment.

## Setup your IDE

You'll now want to point your IDE to use the python interpreter of your new environment, rather than the default interpreter (likely the global python interpreter).

The following steps are for VS Code. If you're not using VS Code, please read your IDE's documentation on selecting python interpreters.

1. Open the `viam-python` directory in VS Code
1. Open the Command Palette (using `⇧⌘P` or through the menus View -> Command Palette)
1. Select the command `Python: Select Interpreter`. There, you should see all the interpreters available to you. You're looking for one the on you just made: `viam-env`. It will look something like: `Python 3.11.5 ('viam-env': venv) ./viam-env/bin/python`. If you don't see it, click the `Refresh` icon on the top right of the Command Palette.

Your IDE will now recognize all packages installed in this environment.

## Start building!

You are now ready to start using Viam's Python SDK!
