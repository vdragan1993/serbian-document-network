# coding=utf-8
from bs4 import BeautifulSoup


def get_result_links(html):
    """
    Extract urls to search result documents
    :param html: result page html
    :return: list of urls
    """
    ret_val = []

    soup = BeautifulSoup(html, 'html.parser')

    urls = soup.findAll("a", attrs={"ng-if": "item.uuid !== null"})
    for url in urls:
        ret_val.append(url['href'])

    return ret_val
