import json
import os
import pathlib

def expand_aliasing():
    base_path = pathlib.Path()
    with open (os.path.join(base_path, "data", "aliasing.json"), "r", encoding="utf8") as f:
        aliasing_log = json.load(f)

    reversed_log = {}
    for k, v in aliasing_log.items():
        reversed_log[v] = k
        reversed_log[k] = v
    
    with open (os.path.join(base_path, "data", "aliasing2.json"), "w", encoding="utf8") as f:
        json.dump(reversed_log, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    expand_aliasing()