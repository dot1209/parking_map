import json
import os
import pathlib

def identify(name: str):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    with open(os.path.join(data_path, "personal_info.json"), "w", encoding="utf8") as f:
        # ncku_buildings = json.load(f)
        f.write(name)
        f.close()

    return None
