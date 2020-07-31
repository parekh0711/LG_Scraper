import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlretrieve
import os
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("chromedriver", options=chrome_options)

file = "out.txt"
url = "https://www.lgindiasocial.com/microsites/brand-store-web-five/locate.aspx"
driver.get(url)
# state = driver.find_element_by_name("ddlState")
# state_options = [x for x in state.find_elements_by_tag_name("option")]
# for element in state_options:
#     print(element.get_attribute("value"))
#     state.se
state = Select(driver.find_element_by_id("ddlState"))
state_options = [option.get_attribute("value") for option in state.options]

for option in state_options[18:]:
    print("doing", option)
    while 1:
        try:
            state = Select(driver.find_element_by_id("ddlState"))
            time.sleep(2)
            state.select_by_value(option)
            break
        except:
            pass
    time.sleep(2)
    city = Select(driver.find_element_by_id("ddlCity"))
    city_options = [o.get_attribute("value") for o in city.options]
    # print(option, city_options)
    for city_option in city_options[1:]:
        while 1:
            try:
                city = Select(driver.find_element_by_id("ddlCity"))
                time.sleep(2)
                city.select_by_value(city_option)
                break
            except:
                pass
        time.sleep(2)
        district = Select(driver.find_element_by_id("ddllocation"))
        district_options = [o.get_attribute("value") for o in district.options]
        # print(district_options)
        for district_option in district_options[1:]:
            print("doing district: ", district_option)
            district = Select(driver.find_element_by_id("ddllocation"))
            district.select_by_value(district_option)
            time.sleep(2)
            submit = driver.find_element_by_name("btnsubmit")
            submit.click()
            time.sleep(2)
            while 1:
                table = driver.find_element_by_id("dladdress")
                time.sleep(1)
                table = table.find_element_by_tag_name("div")
                if "LG" in table.text:
                    break
            print(
                option,
                city_option,
                district_option,
                table.text.replace("\n", "~"),
                sep="~",
                file=open(file, "a+"),
            )
    print("done")
driver.close()
