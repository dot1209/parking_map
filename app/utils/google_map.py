from bs4 import BeautifulSoup
import json
import os
import pathlib
from time import sleep
from tqdm import tqdm
from selenium import webdriver

if __name__ == "__main__":

    base_path = pathlib.Path().resolve()

    webdriver_path = os.path.join(base_path, "app", "webdriver", "chromedriver.exe")
    data_path = os.path.join(base_path, "app", "data")

    driver = webdriver.Chrome(webdriver_path)
    
    with open(os.path.join(data_path, "ncku_buildings.json"), "r", encoding="utf8") as f:
        ncku_buildings = json.load(f)

    with open(os.path.join(data_path, "parking_location.json"), "r", encoding="utf8") as f:
        ncku_parking = json.load(f)

    with open(os.path.join(data_path, "distance.json"), "r", encoding="utf-8") as f:
        distance_log = json.load(f)

    # google map url format
    # google.com.tw/maps/dir/<start place>/<destination>/<current gps coordinate>
    # use '+' to substitude " " in place name
    # gps coordinate is also fine, for example: 
    # from CSIE building to parking
    # https://www.google.com.tw/maps/dir/國立成功大學資訊工程學系+701台南市東區大學路1號/22.997353,120.221882/<current gps cooridinate>
    
    with tqdm(total=94*22) as pbar:
        for building_zone, buildings in ncku_buildings.items():
            for building in buildings:
                for parking_zone, parking_info in ncku_parking.items():
                    if parking_info == {}:
                        continue
                    for parking_name, parking_coord in parking_info.items():
                        if building in distance_log.keys():
                            if parking_name in distance_log[building].keys():
                                pbar.update(1)
                                continue

                        target_url = "https://www.google.com.tw/maps/dir/"+building+"/"+parking_coord
                        driver.get(target_url)
                        sleep(3)

                        walk_btn = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[4]/button')
                        walk_btn.click()
                        sleep(3)
                        
                        soup = BeautifulSoup(driver.page_source, "html.parser")
                        distance = soup.find(
                            "div",
                            class_="xB1mrd-T3iPGc-iSfDt-tUvA6e xB1mrd-T3iPGc-iSfDt-K4efff-text gm2-body-2"
                        )
                        walking_time = soup.find(
                            "div",
                            class_="xB1mrd-T3iPGc-iSfDt-duration gm2-subtitle-alt-1"
                        )

                        if building not in distance_log.keys():
                            distance_log[building] = {}
                        info = {
                            "distance": distance.text,
                            "walking_time": walking_time.text,
                            "zone": parking_zone
                        }
                        distance_log[building][parking_name] = info
                        print(f"{building} -> {parking_name}: {info}")   
                        pbar.update(1)

                        with open(os.path.join(data_path, "distance.json"), "w", encoding="utf8") as f:
                            json.dump(distance_log, f, ensure_ascii=False, indent=4)