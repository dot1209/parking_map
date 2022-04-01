import json
import os
import pathlib
import header

# revise personal info
# input: apply/personal/success
def modify_personal_info(textInfo):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    objstr = textInfo.toJSON()
    json.dump(json.loads(objstr), open(data_path + "/personal_info.json", "w"))     
    

    return None

# show personal info
# output: apply/personal/personal
def show_personal_info():
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")
    
    return json.load(open(data_path + "/personal_info.json"))
