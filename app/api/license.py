import json
import os
import pathlib
import header


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

# show license info
# output: apply/license/license
# output: apply/license/info (in detail)
def show_license():
    pass

