# coding=utf-8
__author__ = "Dragan Vidakovic"
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import scraper

# browser driver
driver_location = "D:/chromedriver.exe"
# advanced search url
search_url = "http://www.pravno-informacioni-sistem.rs/SlGlasnikPortal/reg/advancedSearch"


def get_sub_register_docs(sub_register_value, result_limit):
    """
    Find all documents of given sub register
    :param sub_register_value: select option value of sub register
    :param result_limit: search result limit
    """
    # data_name
    document_number = 1
    # connect to website
    browser = webdriver.Chrome(driver_location)
    browser.get(search_url)

    # setting result limit
    time.sleep(1)
    limit = Select(browser.find_element_by_id("resultLimit"))
    limit.select_by_value(result_limit)
    time.sleep(0.5)
    # selecting sub register
    sub_register = Select(browser.find_element_by_id("podregistar"))
    sub_register.select_by_value(sub_register_value)
    time.sleep(0.5)

    # sub register area
    area = Select(browser.find_element_by_id("oblast"))
    area_values = [option.get_attribute('value') for option in area.options if option.get_attribute('value') != "-1"]

    for area_value in area_values:
        area.select_by_value(area_value)
        time.sleep(0.5)
        # area group
        group = Select(browser.find_element_by_id("grupa"))
        group_values = [option.get_attribute('value') for option in group.options if option.get_attribute('value') != "-1"]

        for group_value in group_values:
            group.select_by_value(group_value)
            time.sleep(0.5)
            submit = browser.find_element_by_xpath("//button[@type='submit']")
            submit.click()
            time.sleep(1)
            document_urls = scraper.get_result_links(browser.page_source)

            for document_url in document_urls:
                get_document_data("http://www.pravno-informacioni-sistem.rs" + document_url, sub_register_value, document_number)
                document_number += 1

    browser.close()


def get_document_data(document_url, save_directory, document_number):
    """

    :param document_url:
    :param save_directory:
    :param document_number:
    :return:
    """
    browser = webdriver.Chrome(driver_location)
    browser.get(document_url)
    time.sleep(2)

    # extract document meta data if any
    # TODO: mozda probati sa izdvajanjem samo html-a date oblasti
    try:
        view_meta_data = browser.find_element_by_xpath("//a[@ng-click='openActIdCard()']")
        view_meta_data.click()
        time.sleep(0.5)
        #scraper.save_document_data(browser.page_source, save_directory, document_number)
    except:
        pass

    # extract document links if any
    # TODO: mozda probati izdvojiti samo html modala
    try:
        view_refs = browser.find_element_by_xpath("//a[@ng-click='openReferencedActsModal()']")
        view_refs.click()
        time.sleep(0.5)
        scraper.save_document_links(browser.page_source, save_directory, document_number)
        # closing dialog
        browser.switch_to_active_element()
        cancel_button = browser.find_element_by_xpath("//button[@ng-click='cancel()']")
        cancel_button.click()
        time.sleep(0.1)

    except:
        pass

    # extract document text
    view_text = browser.find_element_by_xpath("//button[@ng-click='onOnlyActContentClick()']")
    view_text.click()
    time.sleep(1)

    # switch to new tab
    browser.switch_to_window(browser.window_handles[1])
    scraper.save_document_content(browser.page_source, save_directory, document_number)

    browser.quit()


if __name__ == "__main__":
    """
    Podregistri:
        458 - republicki propisi
        459 - propisi iz oblasti prosvete
        206 - medjunarodni ugovori

    sub_registers = ["458", "459", "206"]
    for sub_register in sub_registers:
        list_of_links = get_sub_register_docs(sub_register, "500")
        writer.write_list_of_links(sub_register, list_of_links)
        time.sleep(120)
    """
    get_sub_register_docs("458", "500")
