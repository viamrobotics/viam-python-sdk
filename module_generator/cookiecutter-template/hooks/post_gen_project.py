import sys
import subprocess


if __name__ == "__main__":
    subprocess.run(
        [sys.executable, "../generate_main.py"] + ["{{cookiecutter.__resource_type}}",
                                                   "{{cookiecutter.__resource}}",
                                                   "{{cookiecutter.model_name}}",
                                                   "{{cookiecutter.namespace}}",
                                                   "{{cookiecutter.module_name}}"]
    )
