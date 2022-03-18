import json
import os
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from api import buildings

app = FastAPI()

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/static/css", StaticFiles(directory="static/css"), name="css")
app.mount("/static/js", StaticFiles(directory="static/js"), name="js")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

base_path = Path().resolve()

class Item(BaseModel):
    parking_info: Dict[str, str]

@app.get("/")
def read_root():
    return FileResponse(os.path.join(base_path, "templates", "Map.html"))

@app.get("/Map")
def read_map():
    return FileResponse(os.path.join(base_path, "templates", "Map.html"))

@app.get("/Info")
def read_info():
    return FileResponse(os.path.join(base_path, "templates", "Info.html"))

@app.get("/Apply")
def read_apply():
    return FileResponse(os.path.join(base_path, "templates", "Apply.html"))

@app.get("/apply/chart")
def read_apply_chart():
    return FileResponse(os.path.join(base_path, "templates", "apply", "chart.html"))

@app.get("/apply/license")
def read_apply_license():
    return FileResponse(os.path.join(base_path, "templates", "apply", "license.html"))

@app.get("/apply/personal")
def read_apply_personal():
    return FileResponse(os.path.join(base_path, "templates", "apply", "personal.html"))

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