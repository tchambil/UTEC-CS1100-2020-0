import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
            "edad": "25",
    }
}

with open("data_file.json", "w") as file:
    json.dump(data, file)

json_string = json.dumps(data, indent=4)
print(json_string)