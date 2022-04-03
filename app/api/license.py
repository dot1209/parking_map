import json
import os
import pathlib
import header

load_info = None

# add new license
def add_license(objInfo: header.motorInfo):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    new_license = header.motorObjtoDict(objInfo)
    objstr = ""
    with open(data_path + "/license_info.json", "r") as f:
        objstr = f.read()
        f.close()
    motor_obj = header.motorInfos()
    motor_obj.create_dict(objstr)
    motor_obj.motors[new_license["order"]] = new_license
    with open(data_path + "/license_info.json", "w") as f:
        f.write(motor_obj.dicttoJSON())
        f.close()

    return None

# show multi license infos
# output: apply/license/license
# output: apply/license/info (in detail)
def show_licenses():
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    objstr = ""
    motor_obj = header.motorInfos()
    with open(data_path + "/license_info.json", "r") as f:
        objstr = f.read()
        f.close()
    motor_obj.create_dict(objstr)
    
    return motor_obj

def get_button_key(info: header.detailInfo):
    load_info = info
    return None

"""
# show single license info in detail
def show_license():
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")
    
    personal_id: str
    car_id: str
    car_brand: str
    car_color: str
    car_order: str
    car_class: str
    cost: str
    isNew: str
    isVerify: str
    payAccount: str
    dueDate: str
    isValid: str
    owner: str
    updateDate: str
    updateTime: str
    updateIP: str
    obj = detailInfo()
    with open(data_path + "/license_info.json", "r") as f:
"""





