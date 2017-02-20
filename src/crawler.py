# coding=utf-8
__author__ = "Dragan Vidakovic"
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import writer
import scraper

# browser driver
driver_location = "D:/chromedriver.exe"
# advanced search url
search_url = "http://www.pravno-informacioni-sistem.rs/SlGlasnikPortal/reg/advancedSearch"


def get_sub_register_docs(sub_register_value, result_limit):
    """
    Find url of all documents
    :param sub_register_value: select option value of sub register
    :param result_limit: search result limit
    :return: list of urls
    """
    ret_val = []
    # connect to website
    browser = webdriver.Chrome(driver_location)
    browser.get(search_url)

    # setting result limit
    time.sleep(1)
    limit = Select(browser.find_element_by_id("resultLimit"))
    limit.select_by_value(result_limit)
    time.sleep(1)
    # selecting sub register
    sub_register = Select(browser.find_element_by_id("podregistar"))
    sub_register.select_by_value(sub_register_value)
    time.sleep(1)

    # sub register area
    area = Select(browser.find_element_by_id("oblast"))
    area_values = [option.get_attribute('value') for option in area.options if option.get_attribute('value') != "-1"]

    for area_value in area_values:
        area.select_by_value(area_value)
        time.sleep(1)
        # area group
        group = Select(browser.find_element_by_id("grupa"))
        group_values = [option.get_attribute('value') for option in group.options if option.get_attribute('value') != "-1"]

        for group_value in group_values:
            group.select_by_value(group_value)
            time.sleep(1)
            submit = browser.find_element_by_xpath("//button[@type='submit']")
            submit.click()
            time.sleep(3)
            temp_val = scraper.get_result_links(browser.page_source)
            ret_val += temp_val
            time.sleep(1)

    browser.close()
    print("Rezultata: ")
    print(len(ret_val))
    print()
    return ret_val


if __name__ == "__main__":
    """
    Podregistri:
        458 - republicki propisi
        459 - propisi iz oblasti prosvete
        206 - medjunarodni ugovori
    """
    sub_registers = ["458", "459", "206"]
    for sub_register in sub_registers:
        list_of_links = get_sub_register_docs(sub_register, "500")
        writer.write_list_of_links(sub_register, list_of_links)
        time.sleep(120)
