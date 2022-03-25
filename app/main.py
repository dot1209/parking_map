import json
import os
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from api import buildings, parking, zone

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
    return FileResponse(os.path.join(base_path, "templates", "index.html"))

@app.get("/Map")
def read_map():
    return FileResponse(os.path.join(base_path, "templates", "Map.html"))

@app.get("/Map/{zone}")
def read_map(zone: str):
    return FileResponse(os.path.join(base_path, "templates", "Map", zone + ".html"))

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

@app.get("/distance/{target_name}")
def read_buildings(target_name: str):
    return buildings.get_nearest_parking(target_name, 3)

@app.get("/zone/{building_name}")
def read_zone(building_name: str):
    return zone.find_zone(building_name)
