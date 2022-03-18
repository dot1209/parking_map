import json
import os
import pathlib

def alias(name: str):
    pass

def find_zone(name: str):
    base_path = pathlib.Path().resolve()

    data_path = os.path.join(base_path, "data")

    with open(os.path.join(data_path, "ncku_buildings.json"), "r", encoding="utf8") as f:
        ncku_buildings = json.load(f)

    for buildings_zone, buildings in ncku_buildings.items():
        for building in buildings:
            if building == name:
                return buildings_zone
    return None

if __name__ == "__main__":
    print(find_zone("701台南市東區學人宿舍"))