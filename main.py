import json

with open("config.json") as f:
    config = json.load(f)
    token_key = config["token_key"]
    json_file = config["json_file"]

with open(json_file) as f:
    data = json.load(f)

tokens = []
for key in data.keys():
    if token_key in data[key]:
        tokens.append(str(data[key][token_key]))

with open("tokens.txt", "w") as f:
    f.write("\n".join(tokens))