import json
import os
import header
from pathlib import Path
from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


from api import distance, zone, login, personal, license, payment

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

@app.get("/login")
def read_login():
    return FileResponse(os.path.join(base_path, "templates", "login.html"))

@app.get("/apply/chart/chart")
def read_apply_chart_chart():
    return FileResponse(os.path.join(base_path, "templates", "apply", "chart", "chart.html"))

@app.get("/apply/license/license")
def read_apply_license_license():
    return FileResponse(os.path.join(base_path, "templates", "apply", "license", "license.html"))

@app.get("/apply/license/button-data")
def read_apply_button_data():
    return license.show_licenses()

@app.post("/apply/license/key-data")
def read_get_button_value(textContent: header.detailInfo):
    return license.get_button_key(textContent)

@app.get("/apply/license/info-data")
def read_detail_data():
    return license.show_license()

@app.get("/apply/license/info")
def read_apply_license_info():
    return FileResponse(os.path.join(base_path, "templates", "apply", "license", "info.html"))

@app.get("/apply/license/create")
def read_apply_license_create():
    return FileResponse(os.path.join(base_path, "templates", "apply", "license", "create.html"))

@app.get("/apply/license/success")
def read_apply_license_success():
    return FileResponse(os.path.join(base_path, "templates", "apply", "license", "success.html"))

@app.get("/apply/personal/personal")
def read_apply_personal_personal():
    return FileResponse(os.path.join(base_path, "templates", "apply", "personal", "personal.html"))

@app.get("/apply/personal/personal-data")
def read_personal_info():
    return personal.show_personal_info()

@app.get("/apply/personal/modify")
def read_apply_personal_modify():
    return FileResponse(os.path.join(base_path, "templates", "apply", "personal", "modify.html"))

@app.get("/apply/personal/success")
def read_apply_personal_success():
    return FileResponse(os.path.join(base_path, "templates", "apply", "personal", "success.html"))

@app.get("/apply/payment/payment")
def read_apply_payment_payment():
    return FileResponse(os.path.join(base_path, "templates", "apply", "payment", "payment.html"))

@app.post("/apply/payment/key-data")
def read_apply_payment_key_data(keyObj: header.keyInfo):
    return payment.select_license(keyObj)

@app.post("/apply/payment/set-show")
def read_apply_payment_set_show(keyObj: header.keyInfo):
    return payment.set_show_license()

@app.post("/apply/payment/set-null")
def read_apply_payment_set_null(keyObj: header.keyInfo):
    return payment.set_null()

@app.get("/distance/{target_name}")
def read_buildings(target_name: str):
    print(target_name)
    return distance.get_nearest_target(target_name, 3)

@app.get("/zone/{building_name}")
def read_zone(building_name: str):
    return zone.find_zone(building_name)

@app.post("/login")
def read_login(textContent: header.Info):
    # print(textContent)
    return textContent

@app.post("/apply/personal/modify")
def read_modify(textContent: header.personInfo):
    return personal.modify_personal_info(textContent)

@app.post("/apply/license/create")
def read_create(textContent: header.motorInfo):
    return license.add_license(textContent)

