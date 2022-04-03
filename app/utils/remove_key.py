import json

if __name__ == "__main__":
    with open("data/building_distance.json", "r", encoding="utf-8") as f:
        log = json.load(f)

    new_log = {}
    for k, v in log.items():
        new_log[k] = {}
        for vk, vv in v.items():
            if vk == "光復平面":
                continue
            new_log[k][vk] = vv

    
    with open("data/building_distance.json", "w", encoding="utf-8") as f:
        json.dump(new_log, f, ensure_ascii=False, indent=4)