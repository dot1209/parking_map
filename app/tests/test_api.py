import json

def test_building_api():
    with open("app/data/parking_distance.json", "r", encoding="utf8") as f:
        parking_distance_log = json.load(f)

    assert(parking_distance_log["醫護大樓"] == parking_distance_log["醫護大樓"])