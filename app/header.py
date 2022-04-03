from pydantic import BaseModel
import json

# total license num(multi-user used)
license_num = 0
# total license num(single-user used)
counter = 0

# login data
class Info(BaseModel):
    # member attribute
    ID: str
    password: str
    verify: str

# personal data
class personInfo(BaseModel):
    # member attribute
    ID: str
    name: str
    dep: str
    tel: str
    email: str

    # member function
    def toJSON(self):
        jsonstr = "{\n"
        jsonstr += "\t\"ID\": " + "\"" + self.ID + "\",\n"
        jsonstr += "\t\"name\": " + "\"" + self.name + "\",\n"
        jsonstr += "\t\"dep\": " + "\"" + self.dep + "\",\n"
        jsonstr += "\t\"tel\": " + "\"" + self.tel + "\",\n"
        jsonstr += "\t\"email\": " + "\"" + self.email + "\"\n"
        jsonstr += "}\n"
        return jsonstr
        """
        additional json object to string method
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        """

# single license data
class motorInfo(BaseModel):
    # member attribute
    ID: str
    brand: str
    color: str
    liClass: str
    # member function
    def toJSON(self):
        jsonstr = "{\n"
        jsonstr += "\t\"ID\": " + "\"" + self.ID + "\",\n"
        jsonstr += "\t\"brand\": " + "\"" + self.brand + "\",\n"
        jsonstr += "\t\"color\": " + "\"" + self.color + "\",\n"
        jsonstr += "\t\"liClass\": " + "\"" + self.liClass + "\"\n"
        jsonstr += "}\n"
        return jsonstr

# multi license data
class motorInfos(BaseModel):
    # member attribute
    counter: str
    motors: dict

    def __init__(self):
        motors = {}
        super().__init__(counter = "000", motors = motors)

    # member function
    def create_dict(self, jsonstr):
        global counter
        self.motors = {}
        license = {}

        for line in jsonstr.splitlines():
            tmp = ""
            for word in line.split():
                print("w: " + word + "\n")
                print("li:\n" + str(license) + "\n")
                if word == "{":
                    license = {}
                elif word == "":
                    pass
                elif word == "},":
                    self.motors[license["order"]] = license
                elif word == "}" and license:
                    self.motors[license["order"]] = license
                else:
                    if tmp == "":
                        if word == "\"order\":" or word == "\"ID\":" or word == "\"brand\":" or word == "\"color\":" or word == "\"liClass\":":
                            tmp = getStr(word)
                    else:
                        if tmp == "order":
                            license["order"] = getStr(word)
                        if tmp == "ID":
                            license["ID"] = getStr(word)
                        elif tmp == "brand":
                            license["brand"] = getStr(word)
                        elif tmp == "color":
                            license["color"] = getStr(word)
                        elif tmp == "liClass":
                            license["liClass"] = getStr(word)
                        tmp = ""
        self.counter = InttoStr(len(self.motors.keys()))
        counter = len(self.motors.keys())

        return None

    def dicttoJSON(self):
        objstr = "{\n"
        dictlen = len(self.motors.items())
        i1 = 0
        for item in self.motors.items():
            objstr += "\t\"" + item[0] + "\": "
            listr = motortoJSON(item[1])
            linenum = len(listr.splitlines())
            i2 = 0
            for line in listr.splitlines():
                if i2 == 0:
                    objstr += "{\n"
                elif i2 == linenum - 1:
                    if i1 == dictlen - 1:
                        objstr += "\t}\n"
                    else:
                        objstr += "\t},\n"
                else:
                    objstr += "\t" + line + "\n"
                i2 += 1
            i1 += 1
        objstr += "}"
        return objstr

# single license info in detail
class detailInfo(BaseModel):
    # member attribute
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

    # member function
    def __init__(self):
        super().__init__(personal_id = "",
                         car_id = "",
                         car_brand = "",
                         car_color = "",
                         car_order = "",
                         car_class = "",
                         cost = "",
                         isNew = "",
                         isVerify = "",
                         payAccount = "",
                         dueDate = "",
                         isValid = "",
                         owner = "",
                         updateDate = "",
                         updateTime = "",
                         updateIP = "")


# license (motor's element) dictionary to json
def motortoJSON(obj):
    jsonstr = "{\n"
    jsonstr += "\t\"order\": " + "\"" + obj["order"] + "\",\n"
    jsonstr += "\t\"ID\": " + "\"" + obj["ID"] + "\",\n"
    jsonstr += "\t\"brand\": " + "\"" + obj["brand"] + "\",\n"
    jsonstr += "\t\"color\": " + "\"" + obj["color"] + "\",\n"
    jsonstr += "\t\"liClass\": " + "\"" + obj["liClass"] + "\"\n"
    jsonstr += "}\n"
    return jsonstr

# motorInfo object to dictionary
def motorObjtoDict(obj):
    global counter
    d = {}
    counter += 1
    d["order"] = InttoStr(counter)
    d["ID"] = obj.ID
    d["brand"] = obj.brand
    d["color"] = obj.color
    d["liClass"] = obj.liClass
    return d

# turn counter value to string
def InttoStr(c):
    firstNum = int(c / 100)
    secondNum = int((c - int(c / 100) * 100) / 10)
    thirdNum = c % 10
    return str(firstNum) + str(secondNum) + str(thirdNum)

# get content within ""
def getStr(s):
    return s.split("\"")[1]


