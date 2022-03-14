import json
import os
from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from api import buildings

class Item(BaseModel):
    parking_info: Dict[str, str]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
base_path = Path().resolve()

@app.get("/")
def read_root():
    base_path = Path().resolve()
    with open(os.path.join(base_path, "templates", "index.html"), "r", encoding="utf8") as f:
        html = f.read()
    return HTMLResponse(html)

@app.get("/buildings/{building_name}")
def read_buildings(building_name: str):
    with open(os.path.join(base_path, "data", "distance.json"), "r", encoding="utf-8") as f:
        distance_log = json.load(f)

    n = 0
    result = []
    for k, v in distance_log[building_name].items():
        result.append({k: v})
        n += 1
    return result