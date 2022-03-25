import json
import os
import pathlib

def expand_aliasing():
    base_path = pathlib.Path()
    with open (os.path.join(base_path, "data", "aliasing.json"), "r", encoding="utf8") as f:
        aliasing_log = json.laod(f)

    reversed_log = {}
    for k, v in aliasing_log.items():
        reversed_log[v] = k
    
    for k, v in reversed_log.items():
        aliasing_log[v] = k
    
    with open (os.path.join(base_path, "data", "aliasing.json"), "r", encoding="utf8") as f:
        json.dump(aliasing_log, f, indent=4, ensure_ascii=False)