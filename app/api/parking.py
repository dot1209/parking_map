# -*- coding:utf-8 -*-
import json

def convert2m(s: str) -> int:
    d = s.split(" ")
    if d[1] == "公里":
        return int(float(d[0]) * 1000)
    else:
        return int(d[0])

def get_nearest_parking(parking_name: str, topn: int):
    result = []
    n = 0
    with open("data/parking_distance.json", "r", encoding="utf-8") as f:
        distance_log = json.load(f)
    sorted_distance = dict(sorted(distance_log[parking_name].items(), key=lambda item: convert2m(item[1]["distance"])))
    for k, v in sorted_distance.items():
        result.append({k: v})
        n += 1
        if n == topn:
            break
    
    return result

if __name__ == "__main__":
    print(get_nearest_parking("雲平地停", topn=3))