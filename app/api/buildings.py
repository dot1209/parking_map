# -*- coding:utf-8 -*-
import json

def convert2m(s: str):
    d = s.split(" ")
    if d[1] == "公里":
        return int(d[0]) * 1000
    else:
        return d[0]

def convert2km(s: str):
    d = s.split(" ")
    if int(d[0]) >= 1000:
        d[0] = round(d[0] / 1000, 1)
        return str(d[0]) + " 公里"
    else:
        return str(d[0]) + " 公尺"

def get_nearest_parking(building_name: str):
    result = []
    with open("data/distance.json", "r", encoding="utf-8") as f:
        distance_log = json.load(f)

    sorted_distance = dict(sorted(distance_log[building_name].items(), key=lambda item: convert2m(item[1]["distance"])))
    for k, v in sorted_distance[building_name].items():
        result.append({k: v})
    
    print(result)
    return result

if __name__ == "__main__":
    get_nearest_parking("醫護大樓")