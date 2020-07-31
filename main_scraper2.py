from bs4 import BeautifulSoup
import requests
import urllib.request
import re

input_file_name = "links.txt"
fptr = open(input_file_name, "r")
f1 = fptr.readlines()
fptr.close()
fp2 = open("main_output.txt", "a+")
for index, url in enumerate(f1[:10]):
    while 1:
        try:
            print("doing", index + 1)
            r = requests.get(url.strip("\n"))
            break
        except:
            "Bad net, trying again"
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup.prettify(), file=open("trial.html", "w", encoding="utf-8"))
    try:
        name = soup.find("div", attrs={"class": "name"}).text
    except:
        name = "not given"
    # print(soup.find("div", attrs={"class": "name"}).text, name)

    try:
        cords = soup.find("section", attrs={"class": "find-service-center detail"})
        longitude, latitude = (
            cords["data-center-longitude"],
            cords["data-center-latitude"],
        )
    except:
        longitude, latitude = "not given", "not given"
    try:
        temp = soup.find("div", attrs={"class": "information-block collapse show"})
    except:
        continue
    try:
        phone = temp.find("span", attrs={"class": "visible-xs"}).text
    except:
        phone = "not given"
    # print(phone)
    # break
    temp = temp.text.split("\n")
    temp = [t for t in temp if t != ""]
    # print(temp)
    office = "not given"
    # phone = "not givem"
    address = "not given"
    products = "not given"
    for t in temp:
        if "Repairable Products" in t:
            products = t.replace("Repairable Products", "")
        elif "Address" in t:
            address = t.replace("Address", "")
            index = 0
            while address[index] != " ":
                index += 1
            address = address[index:]
            try:
                pc = re.search(r"\d\d\d\d\d\d", t)
                pc = pc.group(0)
            except:
                pc = "not given"
        elif "Office hours" in t:
            office = t.replace("Office hours", "")
    cords = latitude + ", " + longitude
    # print(phone)
    # print(name)
    print(
        url.replace("\n", ""),
        name,
        office,
        phone.replace(",", "|"),
        products,
        address,
        pc,
        cords,
        sep="~",
        file=fp2,
    )
    # break
