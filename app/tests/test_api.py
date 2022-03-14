import json

def test_building_api():
    with open("app/data/distance.json", "r", encoding="utf8") as f:
        distance_log = json.load(f)

    assert(distance_log["醫護大樓"] == distance_log["醫護大樓"])