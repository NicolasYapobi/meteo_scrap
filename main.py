#!/usr/bin/env python3
import requests
import os.path
from os import path
import json
import bs4 as BeautifulSoup

def get_request():
    count = 0
    x = requests.get("https://www.lachainemeteo.com/meteo-espagne/ville-1519/previsions-meteo-barcelone-aujourdhui")
    soup = BeautifulSoup.BeautifulSoup(x.text, "html.parser")
    div_bar = soup.find_all("div", {"class": "arrow_box"})
    for box in div_bar:
        if count != 15:
            day = box.find("abbr").text
            numday = box.find("div", {"class": "numDay"}).text
            tempe = box.find("div", {"class": "tempe"})
            tempe_list = list(tempe)
            tempe_max = tempe_list[1].text.replace('°', '')
            tempe_min = tempe_list[3].text.replace('°', '')
            json_obj = {
                "Jour": day + " " + numday,
                "Temperature maximale": tempe_max,
                "Temperature minimale": tempe_min
            }
            write_file(json.dumps(json_obj))
            print(json_obj)
            count += 1

def create_file():
    if path.exists("Méteo.txt"):
        print("Météo.txt exists")
    else:
        file = open("Méteo.txt", "w+")
        file.close()

def write_file(json_obj):
    file = open("Méteo.txt", "a+")
    file.write("\n")
    file.write(json_obj)
    file.close()

def main():
    create_file()
    print("Start scrap")
    get_request()

if __name__ == "__main__":
    main()