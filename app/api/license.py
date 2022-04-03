import json
import os
import pathlib
import header

load_info = None

# add new license
def add_license(objInfo: header.motorInfo):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    objstr = ""
    with open(data_path + "/license_info.json", "r") as f:
        objstr = f.read()
        f.close()
    motor_obj = header.motorInfos()
    motor_obj.create_dict(objstr)
    new_license = header.motorObjtoDict(objInfo)
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
    global load_info
    load_info = info
    return None

# show single license info in detail
def show_license():
    global load_info

    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")
    
    """ unset attribute
    cost: str
    isNew: str
    isVerify: str
    payAccount: str
    dueDate: str
    isValid: str
    updateDate: str
    updateTime: str
    updateIP: str
    """
    
    motor_obj = header.motorInfos()
    with open(data_path + "/license_info.json", "r") as f:
        objstr = f.read()
        f.close()

    # set license info
    motor_obj.create_dict(objstr)
    key = load_info.car_order
    load_info.car_id = motor_obj.motors[key]["ID"]
    load_info.car_brand = motor_obj.motors[key]["brand"]
    load_info.car_color = motor_obj.motors[key]["color"]
    load_info.car_class = motor_obj.motors[key]["liClass"]
    
    # set personal info
    per_obj = json.load(open(data_path + "/personal_info.json"))    
    load_info.personal_id = per_obj["ID"]
    load_info.owner = per_obj["name"]

    return load_info

