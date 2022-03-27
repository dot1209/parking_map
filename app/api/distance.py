# -*- coding:utf-8 -*-
import json

def convert2m(s: str) -> int:
    d = s.split(" ")
    if d[1] == "公里":
        return int(float(d[0]) * 1000)
    else:
        return int(d[0])

def get_nearest_target(target_name: str, topn: int):
    result = []
    n = 0
    is_parking = True

    with open("data/parking_distance.json", "r", encoding="utf-8") as f:
        parking_distance_log = json.load(f)
    with open("data/building_distance.json", "r", encoding="utf-8") as f:
        building_distance_log = json.load(f)
    with open("data/aliasing.json", "r", encoding="utf-8") as f:
        aliasing_log = json.load(f)

    if target_name in aliasing_log.keys():
        target_name = aliasing_log[target_name]

    if target_name in parking_distance_log.keys():
        sorted_distance = dict(sorted(parking_distance_log[target_name].items(), key=lambda item: convert2m(item[1]["distance"])))
    elif target_name in building_distance_log.keys():
        sorted_distance = dict(sorted(building_distance_log[target_name].items(), key=lambda item: convert2m(item[1]["distance"])))
        is_parking = False

    else:
        return {"error": "no results found"}

    for k, v in sorted_distance.items():
        # only return the buildings which are defined in map
        if k in aliasing_log.keys():
            result.append({"target": aliasing_log[k], "info": v})
        else:
            result.append({"target": k, "info": v})
        n += 1

        if n == topn:
            break
    
    return {"is_parking": is_parking, "result": result}

if __name__ == "__main__":
    print(get_nearest_target("生科系館", topn=3))