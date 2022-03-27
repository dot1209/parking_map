import json
import os
import pathlib


def new(string):
   pass 


# read license info
# input: apply/license/success
# name is from frontend
def read_license(name: str):
    base_path = pathlib.Path().resolve()
    data_path = os.path.join(base_path, "data")

    with open(os.path.join(data_path, "license.json"), "w", encoding="utf8") as f:
        # store input as a dict 
        # dump into json



# show license info
# output: apply/license/license
# output: apply/license/info (in detail)
def show_license():


