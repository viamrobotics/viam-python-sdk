import json

data = None
with open("./examples/apis.json") as f:
    data = json.load(f)
with open("code-samples-warning.md", "w") as f:
    f.write("Warning changing any of the following functions will break code samples on")
    f.write(" app if an api for these function changes please contact the fleet team\n")
    f.write("|component|function|\n")
    f.write("|-|-|\n")
    for k, v in data.items():
        f.write(f"|{k}|{v}|\n")
