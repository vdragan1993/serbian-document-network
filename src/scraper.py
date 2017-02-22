# coding=utf-8
from bs4 import BeautifulSoup
import writer


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


def save_document_data(html, save_directory, name):
    """

    :param html:
    :param save_directory:
    :param name:
    :return:
    """
    # preparing writing files
    ids_name = 'data/' + save_directory + '/ids/' + str(name) + '.txt'

    ids = ''

    # writing content
    #writer.write_document(ids_name, ids)


def save_document_links(html, save_directory, name):
    """

    :param html:
    :param save_directory:
    :param name:
    :return:
    """
    links_name = 'data/' + save_directory + '/links/' + str(name) + '.txt'
    links = ''
    #writer.write_document(links_name, links)


def save_document_content(html, save_directory, name):
    """

    :param html:
    :param save_directory:
    :param name:
    :return:
    """
    docs_name = 'data/' + save_directory + '/docs/' + str(name) + '.txt'
    soup = BeautifulSoup(html, 'html.parser')
    docs = soup.find("body")
    docs_text = docs.get_text()
    writer.write_document(docs_name, docs_text)
