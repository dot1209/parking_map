import json
import os
import pathlib
import header

key = ""

# store the key of the license to pay
def select_license(obj: header.keyInfo):
    global key
    key = obj.key
    return None

# set payment info to show
def set_show_license():
    global key
    if not key == "":
        header.pay_data[key]["show"] = "t"
    key = ""
    return None

# set key to "" if not download payment
def set_null():
    global key
    key = ""
    return None
